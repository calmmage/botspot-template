"""App strings registered with botspot i18n (`t()`)."""

from botspot.i18n import get_lang, register_strings, set_lang, t

STRINGS: dict[str, dict[str, str]] = {
    "welcome": {
        "en": (
            "Hello, <b>{name}</b>!\nWelcome to {bot_name}!\nUse /help to see available commands."
        ),
        "ru": ("Привет, <b>{name}</b>!\nДобро пожаловать в {bot_name}!\nКоманды: /help."),
    },
    "help": {
        "en": (
            "This is {bot_name}. Use /start to begin.\n"
            "Available commands:\n"
            "/start — Start the bot\n"
            "/help — Show this help message\n"
            "/ask <question> — Ask the LLM\n"
            "/friends — Friends-only ping\n"
            "/help_botspot — Show Botspot help"
        ),
        "ru": (
            "Это {bot_name}. Начни с /start.\n"
            "Команды:\n"
            "/start — Старт\n"
            "/help — Справка\n"
            "/ask <вопрос> — Спросить LLM\n"
            "/friends — Только для друзей\n"
            "/help_botspot — Справка Botspot"
        ),
    },
    "ask_usage": {
        "en": "Usage: /ask <question>",
        "ru": "Использование: /ask <вопрос>",
    },
    "friends_denied": {
        "en": "This command is for friends and admins only.",
        "ru": "Эта команда только для друзей и админов.",
    },
    "friends_ok": {
        "en": "You are on the friends list. Hello!",
        "ru": "Ты в списке друзей. Привет!",
    },
    "premium_ok": {
        "en": "Paid plan is active. This is the premium demo.",
        "ru": "Платный план активен. Это демо premium.",
    },
}

register_strings(STRINGS)

__all__ = ["t", "set_lang", "get_lang", "STRINGS"]
