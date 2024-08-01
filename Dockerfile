FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

CMD python manage.py migrate \
    && python manage.py collectstatic --noinput\
    && python manage.py shell < create_superuser.py \
    && python manage.py runserver 0.0.0.0:8010
