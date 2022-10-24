# pull official base image
FROM python:3.9


# set work directory
WORKDIR /usr/src/django
COPY . /src

COPY docker/entrypoint/wait.sh /usr/local/bin/wait.sh
RUN chmod +x /usr/local/bin/wait.sh

# install psycopg2 dependencies
RUN apt update && apt install postgresql postgresql-contrib gcc python3-dev musl-dev curl bash -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
