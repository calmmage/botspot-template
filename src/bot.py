from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from botspot.core.bot_manager import BotManager
from calmlib.logging import setup_logger

from src.app import App
from src.router import router as main_router


def main(debug: bool = False) -> None:
    setup_logger(level="DEBUG" if debug else "INFO")

    dp = Dispatcher()
    dp.include_router(main_router)

    app = App()
    dp["app"] = app

    bot = Bot(
        token=app.config.telegram_bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    bm = BotManager(
        bot=bot,
        error_handling={"enabled": True},
        ask_user={"enabled": True},
        bot_commands_menu={"enabled": True},
        llm_provider={"enabled": True},
    )
    bm.setup_dispatcher(dp)

    dp.run_polling(bot)


if __name__ == "__main__":
    import argparse
    import os

    from dotenv import load_dotenv

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    load_dotenv(repo_root / ".env")

    debug = args.debug if args.debug else bool(os.getenv("DEBUG"))
    main(debug=debug)
