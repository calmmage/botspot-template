# Botspot Template

A template for creating Telegram bots using [botspot](https://github.com/calmmage/botspot) - a framework built on top of aiogram that provides useful components and utilities.

## Features

- 🚀 Quick setup with minimal boilerplate
- 🛠 Built-in components for common bot features
- 🔧 Easy configuration via environment variables
- 📝 Command menu management out of the box
- ⚡ Error handling and reporting
- 🔍 Bot URL printing for easy testing

## Quick Start

1. Clone this template:
```bash
git clone https://github.com/calmmage/botspot-template.git your-bot-name
cd your-bot-name
```

2. Install dependencies:
```bash
poetry install
```

3. Set up your environment:
```bash
cp example.env .env
# Edit .env with your bot token and settings
```

4. Run the bot:
```bash
poetry run python run.py
```

## Project Structure

```
.
├── app/
│   ├── app.py          # Core app
│   ├── bot.py          # Bot setup & launcher
│   └── __init__.py
├── example.env         # Example environment variables
├── pyproject.toml     # Project dependencies
├── README.md
└── run.py            # Main entry point - for docker etc.
```

## Configuration

The template uses environment variables for configuration. See `example.env` for available options:

- `TELEGRAM_BOT_TOKEN`: Your bot token from @BotFather
- `BOTSPOT_PRINT_BOT_URL_ENABLED`: Print bot URL on startup
- `BOTSPOT_ERROR_HANDLER_ENABLED`: Enable error handling
- `BOTSPOT_BOT_COMMANDS_MENU_ENABLED`: Enable command menu
- And more...

## Development

1. Install pre-commit hooks:
```bash
pre-commit install
```

2. Run tests:
```bash
poetry run pytest
```

## Docker Support

Build and run with Docker:

```bash
docker-compose up --build
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
