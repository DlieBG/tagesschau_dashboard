from pymongo import MongoClient, cursor
import os

class Mongo:

    def __init__(self):
        self.db = MongoClient(os.getenv('MONGO_URI')).tagesschau

    def get_articles(self) -> cursor.Cursor:        
        return self.db.news.find({})
    
    def get_articles_count(self) -> cursor.Cursor:        
        return self.db.news.count_documents({})
