from pymongo import MongoClient, cursor
import os

class Mongo:

    def __init__(self):
        self.db = MongoClient(os.getenv('MONGO_URI')).tagesschau

    def get_count(self) -> int:
        return self.db.news.count_documents({})

    def get_news(self) -> cursor.Cursor:        
        return self.db.news.find({})
