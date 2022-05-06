from mongo import TagesschauMongoDB
from datetime import datetime
from time import sleep
import requests

class InsertNews():

    def __init__(self) -> None:
        self.db = TagesschauMongoDB()
 
        while True:
            self.news_output_bucket = []
            self.__crawl_articles()
            self.db.insert_news(self.news_output_bucket)
            sleep(10 * 60)

    def __crawl_articles(self) -> None:
        frontpage_news = requests.get('https://www.tagesschau.de/api2').json()['news']

        all_news_raw = requests.get('https://www.tagesschau.de/api2/news').json()
        all_news = all_news_raw['news'] + requests.get(all_news_raw['nextPage']).json()['news']

        self.__insert_frontpage_news(frontpage_news)
        self.__insert_all_news(all_news)

    def __insert_frontpage_news(self, frontepage_news: list) -> None:
        for index, news in enumerate(frontepage_news):
            
            if news.get('externalId', None):
                
                existing_news = self.db.get_news(news['externalId'])

                if not existing_news:
                    news['crawler'] = {
                        'insertTime': datetime.now(),
                        'crawlTime': datetime.now(),
                        'crawlType': 'insert',
                        'frontpageIndex': index,
                        'frontpageStatus': 'in',
                        'allIndex': -1,
                        'allStatus': 'stay out'
                    }

                    self.news_output_bucket.append(news)

    def __insert_all_news(self, all_news: list) -> None:
        for index, news in enumerate(all_news):
            
            if news.get('externalId', None):
                
                existing_news_db = self.db.get_news(news['externalId'])
                
                try:
                    existing_news_bucket = [x for x in self.news_output_bucket if x['externalId'] == news['externalId']][0]
                except:
                    existing_news_bucket = None

                if not existing_news_db and not existing_news_bucket:
                    try:
                        news = requests.get(news['details']).json()
                    except:
                        continue

                    news['crawler'] = {
                        'insertTime': datetime.now(),
                        'crawlTime': datetime.now(),
                        'crawlType': 'insert',
                        'frontpageIndex': -1,
                        'frontpageStatus': 'stay out',
                        'allIndex': index,
                        'allStatus': 'in'
                    }

                    print('Inserted article: ', news['externalId'])
                    self.news_output_bucket.append(news)

                elif existing_news_bucket:
                    existing_news_bucket['crawler']['allIndex'] = index
                    existing_news_bucket['crawler']['allStatus'] = 'in'
