from mongo import NewsApiMongoDB
from datetime import datetime, timedelta
from time import sleep
import requests, os

class InsertNews():

    def __init__(self) -> None:
        self.db = NewsApiMongoDB()

    def crawl_news(self) -> None:
        everything = requests.get('https://newsapi.org/v2/everything', {
            'apiKey': os.getenv('API_KEY'),
            'sources': self.db.get_sources(),
            'pageSize': 100,
            'from': (datetime.now() - timedelta(days=1, minutes=15)),
            'to': (datetime.now() - timedelta(days=1))
        }).json()

        if(everything['totalResults'] > 100):
            print(f'Error {everything["totalResults"]} articles are too much :(')
            self.db.insert_error(everything['totalResults'])

        print(f'Inserted {everything["totalResults"]} articles')
        self.db.insert_news(everything['articles'])
