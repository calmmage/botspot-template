# Botspot Template

A template for creating Telegram bots using [botspot](https://github.com/calmmage/botspot) — components on top of [aiogram](https://docs.aiogram.dev).

Needs **Git**, **Python ≥ 3.12**, **[uv](https://docs.astral.sh/uv/getting-started/installation/)**, and **make**. Default runtime is Homebrew **3.13**.

## Quick start

```bash
git clone https://github.com/calmmage/botspot-template.git your-bot-name
cd your-bot-name
make wizard                 # prints help, uv sync, then make doctor
```

Equivalent: `make setup`. That is the only install path. Setup creates a local `.venv`. It does not write a bot token, start polling, or install a LaunchAgent.

Done when `make doctor` prints `cli: ok`. Doctor and `make test` need no Telegram token.

### Run the bot

```bash
cp example.env .env
# set TELEGRAM_BOT_TOKEN from @BotFather
make run
```

Optional: an LLM key (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`) for `/ask`. MongoDB if you enable `user_data`, `access_control`, `subscription_manager`, queues, or `chat_binder`.

## Project structure

```
.
├── src/
│   ├── app.py           # typed AppConfig + App
│   ├── bot.py           # BotManager + polling
│   ├── router.py        # commands (visibility, t(), /ask, friends-only)
│   ├── i18n.py          # botspot t() strings (en/ru)
│   └── __init__.py
├── run.py               # entry point (docker / make run)
├── example.env          # every current botspot component prefix
├── Makefile             # wizard / setup / doctor / check / test / run
├── pyproject.toml
├── Dockerfile
└── docker-compose.yaml
```

## Configuration

Environment variables. See `example.env` for the full list. Prefixes match `BotspotSettings`:

| Prefix | Component |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather |
| `BOTSPOT_ADMINS_STR` / `BOTSPOT_FRIENDS_STR` | Access lists |
| `BOTSPOT_LLM_PROVIDER_` | LLM `/ask` |
| `BOTSPOT_MONGO_DATABASE_` | MongoDB |
| `BOTSPOT_POSTGRES_DATABASE_` | PostgreSQL |
| `BOTSPOT_USER_DATA_` | User records |
| `BOTSPOT_ACCESS_CONTROL_` | Persistent friends/admins |
| `BOTSPOT_SUBSCRIPTION_MANAGER_` | Credits, Stars, trial |
| `BOTSPOT_I18N_` | en/ru middleware |
| `BOTSPOT_ERROR_HANDLER_` | Global error handler |
| `BOTSPOT_BOT_COMMANDS_MENU_` | Telegram command menu |

Component cheat sheet: [botspot_101.md](botspot_101.md). Library examples: [botspot/examples](https://github.com/calmmage/botspot/tree/main/examples).

## Development

```bash
make doctor    # cli: ok
make test      # pytest, no token
make check     # ruff / vulture / pyright
make run       # needs .env
```

```bash
pre-commit install
```

## Docker

```bash
cp example.env .env
docker compose up --build
```

The compose file starts MongoDB and the bot. The bot image uses `uv sync --frozen` and `run.py`.

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE).
