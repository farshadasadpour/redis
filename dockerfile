FROM python:latest

RUN apt-get update \
    && apt-get install -y --show-progress --auto-remove --no-install-recommends build-essential libcurl4-gnutls-dev librtmp-dev libpq-dev \
    && apt-get clean \
    && apt-get autoclean

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip && \
    pip install -r req.txt

CMD [ "python", "./main.py"]