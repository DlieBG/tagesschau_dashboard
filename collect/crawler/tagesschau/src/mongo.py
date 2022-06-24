from pymongo import MongoClient, cursor
from datetime import datetime
import os

class TagesschauMongoDB:

    def __init__(self) -> None:
        self.db = MongoClient(os.getenv('MONGO_URI')).tagesschau

    def insert_news(self, news: list) -> None:
        for n in news:
            n['date'] = datetime.fromisoformat(str(n['date']))
        
        if(len(news) > 0):
            self.db.news.insert_many(news)

    def update_news(self, news: object) -> None:
        try:
            del(news['_id'])
        except KeyError:
            pass

        news['date'] = datetime.fromisoformat(str(news['date']))
        
        self.db.news.insert_one(news)

    def get_news(self, externalId: str) -> object:
        try:
            return self.db.news.aggregate([
                {
                    '$sort': {
                        '_id': 1
                    }
                },
                { 
                    '$match': { 
                        'externalId': externalId
                    } 
                },
                {
                    '$group': {
                        '_id': '$externalId', 
                        'news': {
                            '$last': '$$ROOT'
                        }
                    }
                }
            ]).next()
        except:
            return None

    def get_news_to_update(self, timestamp: datetime) -> cursor:
        return self.db.news.aggregate([
            {
                '$sort': {
                    '_id': 1
                }
            },
            { 
                '$match': { 
                    'crawler.crawlTime': { 
                        '$gte': timestamp
                    }
                } 
            },
            {
                '$group': {
                    '_id': '$externalId', 
                    'news': {
                        '$last': '$$ROOT'
                    }
                }
            },
            {
                '$match': {
                    'news.crawler.crawlType': {
                        '$not': {
                            '$regex': "delete"
                        }
                    }
                }
            }
        ])
