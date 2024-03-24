FROM python:3.11.6-slim-bullseye

WORKDIR /home/app

COPY requirements.txt requirements.txt

# Install packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]