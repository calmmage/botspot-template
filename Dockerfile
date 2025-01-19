FROM python:3.11-slim-buster

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy only dependency files first
COPY pyproject.toml ./

# Configure poetry and install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi

# Copy application code
COPY app/ .

# Run the bot
CMD ["poetry", "run", "python", "run.py"]