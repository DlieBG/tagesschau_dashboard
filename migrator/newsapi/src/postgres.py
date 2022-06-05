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

    def insert_source(self, source):
        self.cur.execute(f'''
            insert into source(
                "id",
                "name",
                "description",
                "url",
                "category",
                "language",
                "country")
            values ({','.join(['%s' for x in range(7)])});
        ''', (
            source['id'],
            source['name'],
            source['description'],
            source['url'],
            source['category'],
            source['language'],
            source['country']           
        ))

    def insert_news(self, news):
        self.cur.execute(f'''
            insert into news(
                "sourceId",
                "author",
                "title",
                "description",
                "url",
                "urlToImage",
                "publishedAt",
                "content")
            values ({','.join(['%s' for x in range(8)])})
            returning id;
        ''', (
            news['source']['id'],
            news.get('author'),
            news['title'],
            news.get('description'),
            news['url'],
            news.get('urlToImage'),
            news['publishedAt'],
            news['content']
        ))

    def commit(self):
        self.conn.commit()

    def delete_news(self):
        self.cur.execute('delete from news;')
        self.cur.execute('delete from source;')
        self.conn.commit()
