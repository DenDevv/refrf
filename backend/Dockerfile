# Використовуємо slim-образ з Python 3.11
FROM python:3.11-alpine

WORKDIR /app

# Копіюємо файл із зависимостями та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код аплікації
COPY ./app ./app

# Відкриваємо порт 8000 та запускаємо Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
