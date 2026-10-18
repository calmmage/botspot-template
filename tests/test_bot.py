from unittest.mock import MagicMock, patch

from src.bot import main


def test_main_wires_dispatcher_and_polls():
    mock_dp = MagicMock()
    mock_bot = MagicMock()
    mock_bm = MagicMock()
    mock_app = MagicMock()
    mock_app.config.telegram_bot_token.get_secret_value.return_value = "test_token"

    with (
        patch("src.bot.Dispatcher", return_value=mock_dp),
        patch("src.bot.Bot", return_value=mock_bot) as bot_cls,
        patch("src.bot.BotManager", return_value=mock_bm),
        patch("src.bot.App", return_value=mock_app),
        patch("src.bot.setup_logger"),
    ):
        main(debug=True)

    bot_cls.assert_called_once()
    mock_dp.include_router.assert_called_once()
    mock_bm.setup_dispatcher.assert_called_once_with(mock_dp)
    mock_dp.run_polling.assert_called_once_with(mock_bot)
