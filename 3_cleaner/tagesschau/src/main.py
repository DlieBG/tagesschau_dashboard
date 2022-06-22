import psycopg2
import os

class Postgres:

    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('PG_HOST'),
            port=int(os.getenv('PG_PORT')),
            database=os.getenv('PG_DATABASE'),
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PASSWORD'))

        self.cur = self.conn.cursor()

    def __get_news(self):
        return None

    def __get_tags(self, tagesschauId):
        return None

    def __insert_clean_tags(self, tagesschauId):
        return None

    def clean_tags(self):
        return None

    def clean_regionId(self):
        self.cur.execute('update tagesschau set "regionId" = 10 where "sophoraId" like \'wdr-%\';')
