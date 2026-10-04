# Botspot Template

A template for creating Telegram bots using botspot, an aiogram framework with batteries included.

Clone, set `TELEGRAM_BOT_TOKEN`, run. The library is [botspot](https://github.com/calmmage/botspot). This repo is the starter.

## Install

Needs **Python ≥ 3.12**, **[uv](https://docs.astral.sh/uv/)**, **make**, and a bot token from [@BotFather](https://t.me/BotFather).

```bash
git clone https://github.com/calmmage/botspot-template.git your-bot-name
cd your-bot-name
make setup                 # uv sync --group extras --group test
cp example.env .env        # set TELEGRAM_BOT_TOKEN
uv run python src/bot.py
```

Or **[Use this template](https://github.com/calmmage/botspot-template/generate)** on GitHub.

See the [README](../README.md) for badges, the hero screenshot, and the agents pointer.

## What ships

- `src/bot.py` — [aiogram](https://docs.aiogram.dev) `Bot` + `BotManager` (error handler, `ask_user`, command menu)
- `src/router.py` — `@botspot_command` `/start` and `/help` via `send_safe`
- `example.env` — `BOTSPOT_` component flags (placeholders only)
- `make test` — `uv run pytest src tests`

Component usage examples live in the library: [botspot examples](https://github.com/calmmage/botspot/tree/main/examples). Snippets in this repo: [botspot_101.md](../botspot_101.md).

**Agents:** [botspot AGENTS.md](https://github.com/calmmage/botspot/blob/main/AGENTS.md).

## Docs in this repo

| | |
|---|---|
| Public README | [README.md](../README.md) |
| Component snippets | [botspot_101.md](../botspot_101.md) |
| Logo / favicon / hero | [docs/examples/](examples/) |
| Library | [calmmage/botspot](https://github.com/calmmage/botspot) |
| Vulnerability reports | [GitHub private advisories](https://github.com/calmmage/botspot-template/security/advisories/new) |

Docs stay in this repository and are linked from the README. GitHub Pages is not used.
