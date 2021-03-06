FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  && apt-get install -y libmysqlclient-dev \	
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip setuptools

RUN mkdir /app
WORKDIR /app
# Installing OS Dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD sgt/ /app/
# Django service
EXPOSE 8000