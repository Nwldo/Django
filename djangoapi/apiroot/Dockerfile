FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

 ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install pipenv
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./Pipfile /usr/src/app/Pipfile


RUN apt-get update && apt-get upgrade -y && apt-get install gcc