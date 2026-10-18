from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from botspot.commands_menu import Visibility, botspot_command
from botspot.llm_provider import aquery_llm_text
from botspot.utils import is_admin, is_friend, send_safe, strip_command

from src.app import App
from src.i18n import t

router = Router()


@botspot_command("start", "Start the bot", visibility=Visibility.PUBLIC)
@router.message(CommandStart())
async def start_handler(message: Message, app: App):
    assert message.from_user is not None
    await send_safe(
        message.chat.id,
        t("welcome", name=message.from_user.full_name, bot_name=app.name),
    )


@botspot_command("help", "Show this help message", visibility=Visibility.PUBLIC)
@router.message(Command("help"))
async def help_handler(message: Message, app: App):
    await send_safe(message.chat.id, t("help", bot_name=app.name))


@botspot_command("ask", "Ask the LLM", visibility=Visibility.PUBLIC)
@router.message(Command("ask"))
async def ask_handler(message: Message):
    question = strip_command(message.text or "")
    if not question:
        await send_safe(message.chat.id, t("ask_usage"))
        return
    user_id = message.from_user.id if message.from_user else None
    reply = await aquery_llm_text(
        prompt=question,
        user=user_id,
        system_message="You are a helpful AI assistant. Keep answers concise.",
    )
    await send_safe(message.chat.id, reply)


@botspot_command("friends", "Friends-only ping", visibility=Visibility.HIDDEN)
@router.message(Command("friends"))
async def friends_handler(message: Message):
    user = message.from_user
    if user is None or not (is_friend(user) or is_admin(user)):
        await send_safe(message.chat.id, t("friends_denied"))
        return
    await send_safe(message.chat.id, t("friends_ok"))


# subscription_manager is on botspot main. Uncomment after enabling MongoDB and:
#   BOTSPOT_SUBSCRIPTION_MANAGER_ENABLED=true
#
# from botspot.subscription_manager import require_plan
#
# @require_plan()
# @botspot_command("premium", "Paid-plan demo", visibility=Visibility.PUBLIC)
# @router.message(Command("premium"))
# async def premium_handler(message: Message):
#     await send_safe(message.chat.id, t("premium_ok"))
