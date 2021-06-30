FROM python:3.8-slim-buster

RUN mkdir /efrastories
COPY requirements.txt /efrastories
WORKDIR /efrastories
RUN pip3 install -r requirements.txt

COPY . /efrastories

RUN chmod u+x ./entrypoint.sh
CMD ["./entrypoint.sh"]