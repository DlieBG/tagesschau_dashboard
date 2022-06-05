FROM python:3.10.4
WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py .
COPY src/mongo.py .
COPY src/newsapi.py .
COPY src/insert_news.py .
COPY src/insert_historic_news.py .
COPY src/process_errors.py .
COPY sources.json sources.json

CMD [ "python", "main.py" ]
