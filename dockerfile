# Используем официальный Python-образ в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Запускаем тесты после сборки
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
