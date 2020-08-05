FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHOHNUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
#EXPOSE 8080

ENV TZ Europe/Moscow

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#CMD ["gunicorn", "vacancy_stepik.wsgi:application", "--bind", "0.0.0.0:8000"]