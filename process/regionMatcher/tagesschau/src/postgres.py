import psycopg2
import os

class Postgres:

    def __init__(self):
        self.conn = psycopg2.connect(
            host = os.getenv('PG_HOST'),
            port = int(os.getenv('PG_PORT')),
            database = os.getenv('PG_DATABASE'),
            user = os.getenv('PG_USER'),
            password = os.getenv('PG_PASSWORD'))

        self.cur = self.conn.cursor()

    def get_tagesschauIds(self):
        self.cur.execute('''select distinct "id" from tagesschau where "crawlerCrawlType"='insert';''')
        return [x[0] for x in self.cur.fetchall()]

    def get_regionIds(self, tagesschauId):
        self.cur.execute('''select "regionId" from tagesschau where "id" = %s''', (tagesschauId,))
        return [x[0] for x in self.cur.fetchall()]

    def get_dates(self, tagesschauId):
        self.cur.execute('''select "date" from tagesschau where "id" = %s''', (tagesschauId,))
        return [x[0] for x in self.cur.fetchall()]

    def insert_clean_region(self, tagesschauId, region, date):
            self.cur.execute('''
                insert into clean_regions(
                    "tagesschauId",
                    "regionId",
                    "regionName",
                    "regionIsoCode",
                    "date"
                    )
                values (%s, %s, %s, %s, %s);
            ''', (
                tagesschauId,
                region.id,
                region.name,
                region.isoCode,
                date
            ))
    
    def delete_clean_regions(self):
        print("Deleting clean_regions")
        self.cur.execute('delete from clean_regions;')
        self.conn.commit()

    def commit(self):
        self.conn.commit()