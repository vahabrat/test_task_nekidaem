# Вытаскиваем базовый образ
FROM python:3.8

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Создаем папку(рабочий каталог)
RUN mkdir /code
# Настраиваем рабочий каталог
WORKDIR /code
# Устанавливаем зависимости
ADD requirements.txt /code/
RUN pip install -r requirements.txt

#RUN python manage.py migrate
# Копируем проект
COPY . /code/

CMD ["python3", "manage.py"]