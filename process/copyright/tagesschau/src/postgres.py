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
        self.cur.execute('''
            select "id", "teaserImageCopyright"
            from tagesschau as t1
            where
                t1."teaserImageCopyright" is not null and
                t1."crawlerCrawlType" = 'insert'
                
            union

            select "id", "teaserImageCopyright"
            from tagesschau as t2
            where 
                t2."teaserImageCopyright" is not null and
                t2."crawlerCrawlType" = 'update' and
                (
                    select "teaserImageCopyright"
                    from tagesschau as sub 
                    where 
                        sub."externalId" = t2."externalId" and
                        sub."crawlerCrawlTime" < t2."crawlerCrawlTime"
                    order by "crawlerCrawlTime" desc
                    limit 1
                ) != t2."teaserImageCopyright";
        ''')
        return self.cur.fetchall()

    def insert_clean_copyright(self, tagesschauId, imageCopyright):
            self.cur.execute('''
                insert into clean_copyright(
                    "tagesschauId",
                    "imageCopyright")
                values (%s, %s);
            ''', (
                tagesschauId,
                imageCopyright
            ))
    
    def delete_clean_copyright(self):
        print("Deleting clean_copyright")
        self.cur.execute('delete from clean_copyright;')
        self.conn.commit()

    def commit(self):
        self.conn.commit()
