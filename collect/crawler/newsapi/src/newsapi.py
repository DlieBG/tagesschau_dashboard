from mongo import NewsApiMongoDB
from datetime import datetime, timedelta
from time import sleep
import requests, os

class NewsApi():

    def __init__(self) -> None:
        self.db = NewsApiMongoDB()

    def crawl_news(self, start: datetime, end: datetime, apiKey: str) -> None:
        try:
            everything = requests.get('https://newsapi.org/v2/everything', {
                'apiKey': apiKey,
                'sources': self.db.get_sources(),
                'pageSize': 100,
                'from': start,
                'to': end
            }).json()
            
            if everything['status'] == 'error':
                self.db.insert_error(0, start, end)
                return None
            
            if(everything['totalResults'] > 100):
                print(f'Error {everything["totalResults"]} articles are too much :(')
                self.db.insert_error(everything['totalResults'], start, end)

            articles = [article for article in everything['articles'] if not self.db.exists(article)]
            
            print(f'Inserted {len(articles)} articles')
            self.db.insert_news(articles)
            return len(everything['articles'])
        except Exception as e:
            print(e)
            self.db.insert_error(0, start, end)
            return None
            