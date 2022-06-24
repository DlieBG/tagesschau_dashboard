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

    def getTexts(self):
        self.cur.execute('''
SELECT tagesschau."id", string_agg(content."value", ' ' ORDER BY content."index")
FROM tagesschau
JOIN content
ON content."tagesschauId" = tagesschau."id"
WHERE tagesschau."crawlerCrawlType" = 'insert'
GROUP BY tagesschau."id";
                         ''')
        return self.cur.fetchall()
