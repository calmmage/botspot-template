import pytest


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test_token")


def test_imports():
    from src.bot import main, dp

    assert main
    assert dp
