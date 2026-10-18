"""Shared pytest configuration."""

import os

import pytest


@pytest.fixture(autouse=True)
def _set_dummy_env_vars(monkeypatch):
    """Dummy env so AppConfig does not fail when TELEGRAM_BOT_TOKEN is unset."""
    if "TELEGRAM_BOT_TOKEN" not in os.environ:
        monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test_token")


@pytest.fixture(autouse=True)
def _reset_i18n_lang():
    from src.i18n import set_lang

    set_lang("en")
    yield
    set_lang("en")
