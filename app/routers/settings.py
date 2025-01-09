from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from botspot.components.bot_commands_menu import add_command
from botspot.utils import reply_safe, answer_safe
from botspot.components.ask_user_handler import ask_user, ask_user_choice

router = Router()

TIMEZONE_SETUP_METHODS = [
    "Enter timezone name (e.g. 'Europe/London')",
    "Send location",
    "Select from common timezones"
]

COMMON_TIMEZONES = [
    "UTC",
    "Europe/London",
    "Europe/Paris",
    "America/New_York",
    "Asia/Tokyo"
]


@add_command("timezone", "Set your timezone")
@router.message(Command("timezone"))
async def timezone_setup(message: Message, state) -> None:
    """Interactive timezone setup with multiple input methods"""
    
    # First, ask user how they want to set their timezone
    method = await ask_user_choice(
        message.chat.id,
        "How would you like to set your timezone?",
        TIMEZONE_SETUP_METHODS,
        state
    )
    
    if not method:
        await reply_safe(message, "Timezone setup cancelled.")
        return

    if method == TIMEZONE_SETUP_METHODS[0]:  # Manual entry
        timezone = await ask_user(
            message.chat.id,
            "Please enter your timezone (e.g. 'Europe/London'):",
            state
        )
        if timezone:
            # Here you would validate the timezone and save it
            await reply_safe(message, f"Timezone set to: {timezone}")
        else:
            await reply_safe(message, "Timezone setup cancelled.")

    elif method == TIMEZONE_SETUP_METHODS[1]:  # Location
        await reply_safe(
            message,
            "Please send your location. Note: This feature is not implemented yet."
        )
        # You would implement location handling here
        
    elif method == TIMEZONE_SETUP_METHODS[2]:  # Common list
        timezone = await ask_user_choice(
            message.chat.id,
            "Select your timezone:",
            COMMON_TIMEZONES,
            state
        )
        if timezone:
            await reply_safe(message, f"Timezone set to: {timezone}")
        else:
            await reply_safe(message, "Timezone setup cancelled.")


@add_command("error_test", "Test error handling")
@router.message(Command("error_test"))
async def error_test(message: Message) -> None:
    """Demonstrate error handling"""
    raise ValueError("This is a test error!") 