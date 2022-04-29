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
        self.conn.autocommit = False

        self.cur = self.conn.cursor()

    def __del__(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
    
    def insert_article(self, article):
        self.cur.execute('''
            insert into news(
                "sophoraId",
                "externalId",
                title,
                "teaserImageTitle",
                "teaserImageCopyright",
                "teaserImageAlttext",
                "teaserImageType",
                date,
                "updateCheckUrl",
                "regionId",
                details,
                "detailsweb",
                topline,
                "firstSentence",
                ressort,
                type,
                "breakingNews",
                index,
                "insertTime",
                "crawlTime",
                "crawlType")
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            returning id;
        ''', (
            article['sophoraId'],
            article['externalId'],
            article['title'],
            article.get('teaserImage', {}).get('title', ''),
            article.get('teaserImage', {}).get('copyright', ''),
            article.get('teaserImage', {}).get('alttext', ''),
            article.get('teaserImage', {}).get('type', ''),
            article['date'],
            article['updateCheckUrl'],
            article['regionId'],
            article['details'],
            article['detailsweb'],
            article['topline'],
            article['firstSentence'],
            article.get('ressort', ''),
            article['type'],
            article['breakingNews'],
            article['crawler']['allIndex'],
            article['crawler']['insertTime'],
            article['crawler']['crawlTime'],
            article['crawler']['crawlType']
        ))

        newsId = self.cur.fetchone()[0]

        if(article.get('content')):
            self.__insert_content(newsId, article['content'])

        if(article.get('geotags')):
            self.__insert_geotags(newsId, article['geotags'])

        if(article.get('tags')):
            self.__insert_tags(newsId, article['tags'])
        
        #self.conn.commit()

    def delete_articles(self):
        self.cur.execute('delete from tags;')
        self.cur.execute('delete from geotags;')
        self.cur.execute('delete from content;')
        self.cur.execute('delete from news;')
        self.conn.commit()

    def __insert_content(self, newsId, contents):
        for index, content in enumerate(contents):
            self.cur.execute('''
                insert into content(
                    "newsId",
                    value,
                    type,
                    index)
                values (%s, %s, %s, %s);
            ''', (
                newsId,
                content.get('value', ''),
                content['type'],
                index
            ))

    def __insert_geotags(self, newsId, geotags):
        for index, geotag in enumerate(geotags):
            self.cur.execute('''
                insert into geotags(
                    "newsId",
                    tag,
                    index)
                values (%s, %s, %s);
            ''', (
                newsId,
                geotag['tag'],
                index
            ))

    def __insert_tags(self, newsId, tags):
        for index, tag in enumerate(tags):
            self.cur.execute('''
                insert into tags(
                    "newsId",
                    tag,
                    index)
                values (%s, %s, %s);
            ''', (
                newsId,
                tag['tag'],
                index
            ))
