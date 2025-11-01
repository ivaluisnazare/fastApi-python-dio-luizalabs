FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

WORKDIR $APP_HOME

# Criar um usuário não-root
RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Mudar proprietário do diretório da aplicação
RUN chown -R appuser:appuser $APP_HOME

# Mudar para usuário não-root
USER appuser

EXPOSE 8000

CMD ["uvicorn", "controller:app", "--host", "0.0.0.0", "--port", "8000"]