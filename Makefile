.PHONY: help wizard setup doctor run test

help:
	@echo "Available targets:"
	@echo "  wizard       - Agent install: print this help, then make setup"
	@echo "  setup        - uv sync --group extras --group test, then make doctor (only install path)"
	@echo "  doctor       - Import src + import fixtures (prints cli: ok)"
	@echo "  run          - Makefile recipe: uv run python src/main.py (that file is missing; live entry is src/bot.py)"
	@echo "  test         - Run pytest on src and tests"
	@echo "  help         - Show this help message"
	@echo "Needs Python 3.12+ and uv on PATH. First setup needs network"
	@echo "and creates .venv here. Doctor needs no Telegram token; no LaunchAgent."

wizard:
	@$(MAKE) help
	@echo "Agent install wizard — the steps live in AGENTS.md."
	@echo "  1. open AGENTS.md"
	@echo "  2. this target runs: make setup"
	@echo ""
	@$(MAKE) setup
	@echo ""
	@echo "Done when: \`make doctor\` prints \`cli: ok\`."
	@echo "Offline (no Telegram token): make doctor"
	@echo "Live bot (human): cp example.env .env, set TELEGRAM_BOT_TOKEN, then uv run python src/bot.py"

setup:
	@command -v uv >/dev/null 2>&1 || { printf '%s\n' 'uv is required on PATH; see https://docs.astral.sh/uv/' >&2; exit 1; }
	uv sync --group extras --group test
	@$(MAKE) doctor

doctor:
	UV_OFFLINE=1 uv run --no-sync python -c "import src; print('botspot-template', src.__version__); from src.bot import main; assert main"
	@printf '%s\n' 'cli: ok'
	UV_OFFLINE=1 uv run --no-sync pytest -q tests/test_imports.py
	@printf '%s\n' 'fixtures: ok'

run:
	uv run python src/main.py

test:
	uv run pytest src tests