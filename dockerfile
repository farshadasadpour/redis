FROM python:latest

WORKDIR /usr/app/src

COPY . ./

RUN pip install -r req.txt

CMD [ "python", "./main.py"]