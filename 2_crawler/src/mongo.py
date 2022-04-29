from pymongo import MongoClient
from datetime import datetime
import os

class NewsApiMongoDB:

    def __init__(self) -> None:
        self.db = MongoClient(os.getenv('MONGO_URI')).newsapi

    def insert_news(self, news: list) -> None:
        for n in news:
            n['publishedAt'] = datetime.fromisoformat(str(n['publishedAt']).replace('Z', '.000+00:00'))
        
        if(len(news) > 0):
            self.db.news.insert_many(news)

    def insert_error(self, count: int) -> None:
        self.db.error.insert_one({
            'timestamp': datetime.now(),
            'count': count
        })

    def get_sources(self) -> list:
        return ",".join([x['id'] for x in list(self.db.sources.find({}))])
