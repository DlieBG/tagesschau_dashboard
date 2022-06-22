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
        self.cur.execute('''select distinct "tagesschauId" from tagesschau;''')
        return [x[0] for x in self.cur.fetchall()]

    def get_regions(self, tagesschauId):
        self.cur.execute('''select "regionId" from tagesschau where "tagesschauId" = %s''', (tagesschauId,))
        return [x[0] for x in self.cur.fetchall()]

    def insert_clean_region(self, tagesschauId, region):
        for index, regionId, regionName, regionIsoCode in enumerate(regions):
            self.cur.execute('''
                insert into clean_regions(
                    "tagesschauId",
                    "regionId",
                    "regionName",
                    "regionIsoCode",
                    "index")
                values (%s, %s, %s, %s);
            ''', (
                tagesschauId,
                regionId,
                regionName,
                regionIsoCode,
                index
            ))
    
    def delete_Clean_regions(self):
        self.cur.execute('delete from clean_tags;')
        self.conn.commit()

    def commit(self):
        self.conn.commit()