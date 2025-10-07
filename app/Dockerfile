# pull the official base image
FROM python:3.12-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project dir (app) to WORKDIR (/usr/src/app)
COPY . .

# upgrade pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt
