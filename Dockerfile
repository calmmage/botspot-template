FROM python:3.12-slim-bookworm

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy the entire project files
COPY . .

# Install dependencies with uv sync, including specified groups
RUN uv sync --group extras

# Run the bot
CMD ["uv", "run", "python", "run.py"]