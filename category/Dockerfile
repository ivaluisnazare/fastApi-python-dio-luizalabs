# Use a imagem oficial do Python
FROM python:3.11-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

# Criar diretório da aplicação
WORKDIR $APP_HOME

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de requirements primeiro (para melhor cache do Docker)
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "controller:app", "--host", "0.0.0.0", "--port", "8000"]