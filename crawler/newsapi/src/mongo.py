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
    
    def get_errors(self) -> list:
        list(self.db.error.find({}).limit(4))
    
    def delete_error(self, error_id: str) -> None:
        self.db.error.delete_one({'_id': error_id})

    def insert_error(self, count: int, start: datetime, end: datetime) -> None:
        self.db.error.insert_one({
            'timestamp': datetime.now(),
            'count': count,
            'from': start,
            'to': end,
        })
        
    def exists(self, article: dict) -> bool:
        return self.db.news.find_one({'url': article['url']}) is not None

    def get_sources(self) -> str:
        return ",".join([x['id'] for x in list(self.db.sources.find({}))])

    def insert_sources(self, sources: list) -> None:
        self.db.sources.insert_many(sources)
