from typing import Tuple
from mongo import TagesschauMongoDB
from datetime import datetime, timedelta
from time import sleep
import requests

class UpdateNews():

    def __init__(self) -> None:
        self.db = TagesschauMongoDB()
 
        while True:
            self.__update_news(datetime.now() - timedelta(days=1))
            sleep(10 * 60)

    def __update_news(self, timestamp: datetime) -> None:
        frontpage_news = requests.get('https://www.tagesschau.de/api2').json()['news']

        all_news_raw = requests.get('https://www.tagesschau.de/api2/news').json()
        all_news = all_news_raw['news'] + requests.get(all_news_raw['nextPage']).json()['news']

        for news in self.db.get_news_to_update(timestamp):
            try:
                frontpage_index = self.__find_index(frontpage_news, news['news']['sophoraId'])
                all_index = self.__find_index(all_news, news['news']['sophoraId'])

                update = requests.get(news['news']['updateCheckUrl']).json()

                if update == True or frontpage_index != news['news']['crawler']['frontpageIndex']: # or all_index != news['news']['crawler']['allIndex']:

                    if frontpage_index != -1:
                        if news['news']['crawler']['frontpageIndex'] == -1:
                            frontpage_status = 'in'
                        elif news['news']['crawler']['frontpageIndex'] == frontpage_index:
                            frontpage_status = 'stay in'
                        elif news['news']['crawler']['frontpageIndex'] < frontpage_index:
                            frontpage_status = 'down'
                        elif news['news']['crawler']['frontpageIndex'] > frontpage_index:
                            frontpage_status = 'up'
                    else:
                        if news['news']['crawler']['frontpageIndex'] == -1:
                            frontpage_status = 'stay out'
                        else:
                            frontpage_status = 'out'

                    if all_index != -1:
                        if news['news']['crawler']['allIndex'] == -1:
                            all_status = 'in'
                        elif news['news']['crawler']['allIndex'] == all_index:
                            all_status = 'stay in'
                        elif news['news']['crawler']['allIndex'] < all_index:
                            all_status = 'down'
                        elif news['news']['crawler']['allIndex'] > all_index:
                            all_status = 'up'
                    else:
                        if news['news']['crawler']['allIndex'] == -1:
                            all_status = 'stay out'
                        else:
                            all_status = 'out'
                    
                    if update:
                        new_news = requests.get(news['news']['details']).json()
                    else:
                        new_news = news['news']

                    new_news['crawler'] = {
                        'insertTime': news['news']['crawler']['insertTime'],
                        'crawlTime': datetime.now(),
                        'crawlType': 'update',
                        'contentUpdate': update,
                        'frontpageIndex': frontpage_index,
                        'frontpageStatus': frontpage_status,
                        'allIndex': all_index,
                        'allStatus': all_status
                    }

                    print('Updated article: ', news['news']['sophoraId'])
                    self.db.update_news(new_news)

            except:
                news['news']['crawler'] = {
                    'insertTime': news['news']['crawler']['insertTime'],
                    'crawlTime': datetime.now(),
                    'crawlType': 'delete',
                    'frontpageIndex': -1,
                    'frontpageStatus': 'stay out' if news['news']['crawler']['frontpageStatus'] == 'stay out' or news['news']['crawler']['frontpageStatus'] == 'out' else 'out',
                    'allIndex': -1,
                    'allStatus': 'stay out' if news['news']['crawler']['allStatus'] == 'stay out' or news['news']['crawler']['allStatus'] == 'out' else 'out'
                }

                print('Deleted article: ', news['news']['sophoraId'])
                self.db.update_news(news['news'])

    def __find_index(self, news: list, sophoraId: str) -> int:
        for index, article in enumerate(news):
            if article.get('sophoraId', None) == sophoraId:
                return index

        return -1
