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
        self.cur.execute('''select distinct "tagesschauId" from tags;''')
        return [x[0] for x in self.cur.fetchall()]

    def get_tags(self, tagesschauId):
        self.cur.execute('''select "tag" from tags where "tagesschauId" = %s order by "index";''', (tagesschauId,))
        return [x[0] for x in self.cur.fetchall()]

    def insert_clean_tags(self, tagesschauId, tags):
        for index, tag in enumerate(tags):
            self.cur.execute('''
                insert into clean_tags(
                    "tagesschauId",
                    "tag",
                    "index")
                values (%s, %s, %s);
            ''', (
                tagesschauId,
                tag,
                index
            ))
    
    def delete_clean_tags(self):
        self.cur.execute('delete from clean_tags;')
        self.conn.commit()

    def clean_regionId(self):
        self.cur.execute('''update tagesschau set "regionId" = 10 where "sophoraId" like 'wdr-%';''')
        self.conn.commit()

    def commit(self):
        self.conn.commit()