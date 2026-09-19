from pydantic import SecretStr

from src.app import App, AppConfig


def test_app_config_from_kwargs():
    config = AppConfig(telegram_bot_token=SecretStr("test_token"))
    assert config.telegram_bot_token.get_secret_value() == "test_token"


def test_app_name_and_config():
    app = App(telegram_bot_token=SecretStr("test_token"))
    assert app.name == "Mini Botspot Template"
    assert app.config.telegram_bot_token.get_secret_value() == "test_token"
