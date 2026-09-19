# AGENTS.md — install wizard

If you want to set this up, just copy this to your agent:

```
please set up https://github.com/calmmage/botspot-template according to its instructions. Audit safety and guide me through the setup, bundle and automate everything you can as a setup wizard script, logging what it does.
```

This file is the install wizard for agents. Humans who just want a bot: [README.md](README.md). Makefile targets are the source of truth for commands (`make help`).

Standalone install is done when `make doctor` prints `cli: ok`. Continue to a live Telegram bot only for the features the user requested. Setup does not write a bot token, start polling, or install LaunchAgents.

Do not invent a second installer. The only install path is `make setup` (`make wizard` prints help, points here, then `make setup`).

## 1. Install the package

Needs **[uv](https://docs.astral.sh/uv/getting-started/installation/)**, **make**, and CPython **≥ 3.12** (uv downloads one if the system interpreter is older). If `uv` is missing:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Follow the installer's PATH instructions (or open a new shell), then check `uv --version` before continuing. The first setup needs network access to download dependencies (including git deps [calmlib](https://github.com/calmmage/calmlib) and [botspot](https://github.com/calmmage/botspot)) and, if needed, Python.

Then:

```bash
git clone https://github.com/calmmage/botspot-template.git your-bot-name
cd your-bot-name
make wizard          # prints this file's pointer, then `make setup`
# equivalent: make setup
```

`make setup` requires `uv` on PATH, runs `uv sync`, then `make doctor`. That is the only install path. It creates a local `.venv`. This repo is a Telegram bot template, not a CLI binary; doctor imports `src` and runs `tests/test_imports.py`. Setup does not collect Telegram credentials or install LaunchAgents.

Done when: `uv --version` works and `make doctor` prints `cli: ok`.

Offline without a Telegram token (after install):

```bash
make doctor
```

Doctor uses `uv run --no-sync` with `UV_OFFLINE=1`, so it checks the installed environment without installing packages. Run `make setup` before doctor in a fresh checkout. Doctor must exit 0 and print `cli: ok` (and `fixtures: ok` for the import tests). `tests/test_imports.py` injects a dummy `TELEGRAM_BOT_TOKEN`; it does not need a real token.

## 2. Live bot (human)

The agent cannot complete this step. Copy `example.env` to `.env` and set at least `TELEGRAM_BOT_TOKEN` from [@BotFather](https://t.me/BotFather). The bot entry is `run.py` (`src/bot.py`):

```bash
make run
# equivalent: uv run python run.py
```

Do not install LaunchAgents as part of setup. Do not commit `.env`. MongoDB, LLM keys, and other values in `example.env` are only for a live bot, not for `make doctor`.

Done when: the process starts and Telegram `/start` answers.

## 3. Test

```bash
make test            # uv run pytest tests/ (coverage on src)
```

Done when: `make test` is green. Tests inject dummy `TELEGRAM_BOT_TOKEN`; they do not need a real token.

## 4. Layout

- Entry: `run.py` → `src/bot.py` → `src/router.py` → `src/app.py`
- i18n: `src/i18n.py` (`t()` via botspot)
- Config: `example.env` / `.env` (never commit `.env`)
- Dependencies: `pyproject.toml` + `uv.lock` via `make setup` (`uv sync`) only — not Poetry
- Component snippets: [botspot_101.md](botspot_101.md)
- Vulnerabilities: [SECURITY.md](SECURITY.md)
