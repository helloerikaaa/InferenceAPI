# imagen oficial
FROM python:3.8.10-slim-buster

# agregar el directorio de trabajo
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# agregar variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instalación de dependencias
RUN apt-get update \
&& apt-get -y install netcat gcc \
&& apt-get clean

# instalación de dependencias de python
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy

# copiar código de la aplicación
COPY . .