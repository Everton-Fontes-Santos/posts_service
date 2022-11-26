FROM python:3.9
ENV PYTHONBUFERED 1
WORKDIR ./app
COPY requirements.txt /app/requirements.txt
run pip install -r requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000