from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from calmlib.utils import setup_logger, heartbeat_for_sync
from dotenv import load_dotenv
from loguru import logger

from app._app import App
from app.router import router as main_router
from app.routers.settings import router as settings_router
from botspot.core.bot_manager import BotManager


@heartbeat_for_sync(App.name)
def main(debug=False) -> None:
    setup_logger(logger, level="DEBUG" if debug else "INFO")

    # Initialize bot and dispatcher
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.include_router(settings_router)

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
    repo_root = Path(__file__).parent
    load_dotenv(repo_root / ".env")
    main()
