from newsapi import NewsApi
from datetime import datetime, timedelta
import os

class InsertNews():

    def __init__(self) -> None:
        self.news_api = NewsApi()
        self.api_key = os.getenv('API_KEY')

    def crawl_news(self) -> None:
        start = datetime.now() - timedelta(days=1, minutes=15)
        end = datetime.now() - timedelta(days=1)
        self.news_api.crawl_news(start, end, self.api_key)