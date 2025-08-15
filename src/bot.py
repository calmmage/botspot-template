from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from botspot.core.bot_manager import BotManager
from calmlib.utils import setup_logger
from loguru import logger

from src._app import App
from src.router import router as main_router


# todo: add new calmmage health checks - @heartbeat_for_sync(App.name)
def main(debug=False) -> None:
    setup_logger(logger, level="DEBUG" if debug else "INFO")

    # Initialize bot and dispatcher
    dp = Dispatcher()
    dp.include_router(main_router)

    app = App()
    dp["app"] = app

    # Initialize Bot instance with a default parse mode
    bot = Bot(
        token=app.config.telegram_bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    # Initialize BotManager with default components
    bm = BotManager(
        bot=bot,
        error_handler={"enabled": True},
        ask_user={"enabled": True},
        bot_commands_menu={"enabled": True},
    )

    # Setup dispatcher with our components
    bm.setup_dispatcher(dp)

    # Start polling
    dp.run_polling(bot)


if __name__ == "__main__":
    import argparse
    import os

    from dotenv import load_dotenv

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    repo_root = Path(__file__).parent
    dotenv_path = repo_root / ".env"

    if dotenv_path.exists():
        load_dotenv(dotenv_path)

    debug = args.debug if args.debug else bool(os.getenv("DEBUG"))
    main(debug=debug)
