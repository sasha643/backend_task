FROM python:3.12.2

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry && poetry config virtualenvs.create false 

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    ca-certificates \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libatspi2.0-0 \
    libxshmfence1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_HTTP_TIMEOUT=120

RUN poetry install --no-interaction --no-ansi

RUN poetry run playwright install

COPY . .

RUN mkdir -p /app/data

ENV DATA_DIR=/app/data

RUN python src/seed.py

CMD ["python", "src/main.py"]
