FROM python:3
LABEL maintainer="Alex Puga"

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["python", "sentiment.py"]
