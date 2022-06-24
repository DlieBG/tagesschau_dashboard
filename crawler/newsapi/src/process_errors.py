from mongo import NewsApiMongoDB
from newsapi import NewsApi
from datetime import datetime, timedelta
from time import sleep
import requests, os

class ProcessErrors():

    def __init__(self) -> None:
        self.db = NewsApiMongoDB()
        self.news_api = NewsApi()
        self.api_key = os.getenv('API_KEY')

    def process_errors(self) -> None:
        for error in self.db.get_errors():
            if error['count'] == 0:
                self.news_api.crawl_news(error['from'], error['to'], self.api_key)
                self.db.delete_error(error['_id'])
                continue
            
            delta = error['to'] - error['from']
            end = error['from'] + timedelta(seconds = delta.total_seconds()/2)
            self.news_api.crawl_news(error['from'], end, self.api_key)
            self.db.delete_error(error['_id'])
            self.db.insert_error(0, end, error['to'])
