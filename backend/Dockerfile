# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências para o contêiner
COPY ./requirements.txt /app/requirements.txt

# Copia o código da aplicação para o contêiner
COPY ./app /app

# Instala as dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Expõe a porta para acesso externo
EXPOSE 8000

# Define a variável de ambiente para o Python
ENV PYTHONPATH=/app

# Comando para rodar a aplicação com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
