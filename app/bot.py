from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

from botspot.components.bot_commands_menu import add_command
from botspot.core.bot_manager import BotManager
from botspot.utils import reply_safe

from .routers.settings import router as settings_router

load_dotenv()
TOKEN = getenv("TELEGRAM_BOT_TOKEN")
if TOKEN is None or TOKEN == "":
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

dp = Dispatcher()
dp.include_router(settings_router)


@add_command("start", "Start the bot")
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Send a welcome message when the command /start is issued"""
    await reply_safe(
        message,
        f"Hello, {html.bold(message.from_user.full_name)}!\n\n"
        f"Use /help to see available commands."
    )


@add_command("help", "Show available commands")
@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """Show help message with available commands"""
    await reply_safe(
        message,
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/timezone - Set your timezone\n"
        "/error_test - Test error handling"
    )


async def main() -> None:
    # Initialize Bot instance with a default parse mode
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # Initialize BotManager with default components
    bm = BotManager(
        bot=bot,
        error_handler={"enabled": True},
        ask_user={"enabled": True},
        bot_commands_menu={"enabled": True}
    )
    
    # Setup dispatcher with our components
    bm.setup_dispatcher(dp)
    
    # Start polling
    await dp.start_polling(bot) 