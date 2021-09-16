FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py" ]