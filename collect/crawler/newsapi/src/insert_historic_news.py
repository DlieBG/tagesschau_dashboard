from newsapi import NewsApi
from datetime import datetime, timedelta
import os

class InsertHistoricNews():

    def __init__(self, latest: datetime) -> None:
        self.news_api = NewsApi()
        self.api_key_count = int(os.getenv('API_KEY_COUNT'))
        self.latest = latest

    def crawl_historic_news(self) -> None:
        for api_key_index in range(self.api_key_count):
            for i in range(100):
                api_key = os.getenv(f'API_KEY_{api_key_index}')
                start = self.latest - timedelta(minutes=15)
                result = self.news_api.crawl_news(start, self.latest, api_key)
                self.latest = start
                if result is None:
                    break
