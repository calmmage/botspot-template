import pytest


def test_imports():
    from app.bot import main, dp

    assert main
    assert dp
