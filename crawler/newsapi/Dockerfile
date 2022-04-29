FROM python:3.10.4
WORKDIR /app

COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/main.py .
COPY src/mongo.py .
COPY src/insert_news.py .
COPY sources.json sources.json

CMD [ "python3", "main.py" ]
