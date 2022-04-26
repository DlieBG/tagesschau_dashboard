FROM python:3.10.4
WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py .
COPY src/mongo.py .
COPY src/insert_news.py .
COPY src/update_news.py .

CMD [ "python", "main.py" ]
