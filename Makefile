.PHONY: setup run test

setup:
	uv sync --group extras --group test

run:
	uv run python src/main.py

test:
	uv run pytest src tests