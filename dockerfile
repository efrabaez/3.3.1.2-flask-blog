FROM python:3.8-slim-buster

RUN mkdir /efrastories
COPY requirements.txt /efrastories
WORKDIR /efrastories
RUN pip3 install -r requirements.txt

COPY . /efrastories

CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80"]