from src.i18n import STRINGS, get_lang, set_lang, t


def test_english_welcome():
    set_lang("en")
    text = t("welcome", name="Ada", bot_name="Demo")
    assert "Ada" in text
    assert "Demo" in text


def test_russian_fallback_and_switch():
    set_lang("ru")
    assert "Привет" in t("welcome", name="Ada", bot_name="Demo")
    set_lang("en")
    assert get_lang() == "en"


def test_unknown_key_returns_key():
    assert t("not_a_real_key") == "not_a_real_key"


def test_required_keys_exist():
    for key in ("welcome", "help", "ask_usage", "friends_denied", "friends_ok", "premium_ok"):
        assert key in STRINGS
        assert "en" in STRINGS[key]
        assert "ru" in STRINGS[key]
