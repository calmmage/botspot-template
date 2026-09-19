"""Handler tests — no Telegram token and no live BotManager required."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.app import App
from src.router import ask_handler, friends_handler, help_handler, start_handler


def _message(*, text="/start", user_id=42, full_name="Ada", chat_id=99):
    message = MagicMock()
    message.text = text
    message.chat.id = chat_id
    message.from_user = MagicMock()
    message.from_user.id = user_id
    message.from_user.full_name = full_name
    return message


@pytest.fixture
def app():
    return App(telegram_bot_token="test_token")


@pytest.mark.asyncio
async def test_start_handler(app):
    message = _message(text="/start")
    with patch("src.router.send_safe", new_callable=AsyncMock) as send:
        await start_handler(message, app)
    send.assert_awaited_once()
    body = send.await_args.args[1]
    assert "Ada" in body
    assert app.name in body


@pytest.mark.asyncio
async def test_help_handler(app):
    message = _message(text="/help")
    with patch("src.router.send_safe", new_callable=AsyncMock) as send:
        await help_handler(message, app)
    send.assert_awaited_once()
    body = send.await_args.args[1]
    assert "/ask" in body
    assert app.name in body


@pytest.mark.asyncio
async def test_ask_handler_usage():
    message = _message(text="/ask")
    with patch("src.router.send_safe", new_callable=AsyncMock) as send:
        await ask_handler(message)
    send.assert_awaited_once()
    assert "Usage" in send.await_args.args[1] or "ask" in send.await_args.args[1].lower()


@pytest.mark.asyncio
async def test_ask_handler_queries_llm():
    message = _message(text="/ask what is 2+2")
    with (
        patch("src.router.aquery_llm_text", new_callable=AsyncMock, return_value="4") as llm,
        patch("src.router.send_safe", new_callable=AsyncMock) as send,
    ):
        await ask_handler(message)
    llm.assert_awaited_once()
    assert llm.await_args.kwargs["prompt"] == "what is 2+2"
    send.assert_awaited_once()
    assert send.await_args.args[1] == "4"


@pytest.mark.asyncio
async def test_friends_handler_denied():
    message = _message(text="/friends")
    with (
        patch("src.router.is_friend", return_value=False),
        patch("src.router.is_admin", return_value=False),
        patch("src.router.send_safe", new_callable=AsyncMock) as send,
    ):
        await friends_handler(message)
    send.assert_awaited_once()
    body = send.await_args.args[1]
    assert "friend" in body.lower() or "друг" in body.lower()


@pytest.mark.asyncio
async def test_friends_handler_allowed():
    message = _message(text="/friends")
    with (
        patch("src.router.is_friend", return_value=True),
        patch("src.router.is_admin", return_value=False),
        patch("src.router.send_safe", new_callable=AsyncMock) as send,
    ):
        await friends_handler(message)
    send.assert_awaited_once()
    body = send.await_args.args[1]
    assert "Hello" in body or "Привет" in body
