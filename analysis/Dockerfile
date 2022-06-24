FROM python:3.10.4
WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download de_core_news_sm

COPY src/main.py .
COPY src/textstrip.py .
COPY src/postgres.py .

CMD [ "python", "main.py" ]