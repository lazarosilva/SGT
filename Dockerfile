FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD sgt/ /app/
# Django service
EXPOSE 8000
