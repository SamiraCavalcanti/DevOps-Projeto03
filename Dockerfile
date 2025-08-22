FROM python:3.9-slim

WORKDIR /app

# Copiar e instalar dependências primeiro (para aproveitar cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquivos da aplicação
COPY app.py .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "app.py"]