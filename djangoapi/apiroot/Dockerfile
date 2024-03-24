FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

 ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install pipenv
COPY requirements.txt requirements.txt
RUN pip install -U -r requirements.txt



COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]