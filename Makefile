.PHONY: check fix fix-unsafe help test wizard setup doctor run

run:
	uv run python run.py

run-debug:
	uv run python run.py --debug

help:
	@echo "Available targets:"
	@echo "  wizard       - Agent install: print this help, then make setup"
	@echo "  setup        - uv sync, then make doctor (only install path)"
	@echo "  doctor       - Import src + import fixtures (prints cli: ok)"
	@echo "  run          - Start the bot (needs .env TELEGRAM_BOT_TOKEN)"
	@echo "  check        - Run all linters and type checks (continues past failures)"
	@echo "  fix          - Auto-fix lint issues and format code"
	@echo "  fix-unsafe   - Auto-fix with unsafe fixes enabled"
	@echo "  test         - Run tests with coverage"
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
	@echo "Live bot (human): cp example.env .env, set TELEGRAM_BOT_TOKEN, then make run"

setup:
	@command -v uv >/dev/null 2>&1 || { printf '%s\n' 'uv is required on PATH; see https://docs.astral.sh/uv/' >&2; exit 1; }
	uv sync
	@$(MAKE) doctor

doctor:
	UV_OFFLINE=1 uv run --no-sync python -c "import src; print('project-name', src.__version__); from src.bot import main; assert main"
	@printf '%s\n' 'cli: ok'
	UV_OFFLINE=1 uv run --no-sync pytest -q tests/test_imports.py
	@printf '%s\n' 'fixtures: ok'

check:
	-uv run ruff check src tests
	-uv run ruff format --check src tests
	-uv run vulture --min-confidence 80 src
	-uv run pyright

fix:
	-uv run ruff check --fix .
	uv run ruff format .

fix-unsafe:
	-uv run ruff check --fix --unsafe-fixes .
	uv run ruff format .

test:
	uv run pytest tests/ --cov=src --cov-report=term --cov-fail-under=50
