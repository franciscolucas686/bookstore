# Etapa base com Python
FROM python:3.12.1-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.2

# Instala dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Instala as dependencias do Postgres
RUN apt-get update && \
    apt-get -y install libpq-dev gcc &&\
    pip install psycopg2-binary

# Adiciona o Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Instala as dependências (apenas as principais)
RUN poetry install 

# Copia o restante do projeto
COPY . .

# Expõe a porta do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
