FROM python:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libcurl4-gnutls-dev librtmp-dev libpq-dev \
    && apt-get clean

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip && \
    pip install -r req.txt

CMD [ "python", "./main.py"]