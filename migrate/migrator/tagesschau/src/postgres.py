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

    def insert_news(self, news):
        self.cur.execute('''
            insert into tagesschau(
                "sophoraId",
                "externalId",
                "title",
                "teaserImageTitle",
                "teaserImageCopyright",
                "teaserImageAlttext",
                "teaserImageType",
                "date",
                "trackingSid",
                "trackingSrc",
                "trackingCtp",
                "trackingPdt",
                "trackingOtp",
                "trackingCid",
                "trackingPti",
                "trackingType",
                "updateCheckUrl",
                "regionId",
                "details",
                "detailsweb",
                "shareUrl",
                "topline",
                "firstSentence",
                "ressort",
                "type",
                "breakingNews",
                "crawlerInsertTime",
                "crawlerCrawlTime",
                "crawlerCrawlType",
                "crawlerContentUpdate",
                "crawlerFrontpageIndex",
                "crawlerFrontpageStatus",
                "crawlerAllIndex",
                "crawlerAllStatus")
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            returning id;
        ''', (
            news['sophoraId'],
            news['externalId'],
            news['title'],
            news.get('teaserImage', {}).get('title'),
            news.get('teaserImage', {}).get('copyright'),
            news.get('teaserImage', {}).get('alttext'),
            news.get('teaserImage', {}).get('type'),
            news['date'],
            news['tracking'][0]['sid'],
            news['tracking'][0]['src'],
            news['tracking'][0]['ctp'],
            news['tracking'][0]['pdt'],
            news['tracking'][0]['otp'],
            news['tracking'][0]['cid'],
            news['tracking'][0]['pti'],
            news['tracking'][0]['type'],
            news['updateCheckUrl'],
            news['regionId'],
            news['details'],
            news['detailsweb'],
            news['shareURL'],
            news['topline'],
            news['firstSentence'],
            news.get('ressort'),
            news['type'],
            news['breakingNews'],
            news['crawler']['insertTime'],
            news['crawler']['crawlTime'],
            news['crawler']['crawlType'],
            news['crawler'].get('contentUpdate'),
            news['crawler']['frontpageIndex'],
            news['crawler']['frontpageStatus'],
            news['crawler']['allIndex'],
            news['crawler']['allStatus'],
        ))

        tagesschauId = self.cur.fetchone()[0]

        if(news.get('content')):
            self.__insert_content(tagesschauId, news['content'])

        if(news.get('geotags')):
            self.__insert_geotags(tagesschauId, news['geotags'])

        if(news.get('tags')):
            self.__insert_tags(tagesschauId, news['tags'])

    def commit(self):
        self.conn.commit()

    def delete_news(self):
        self.cur.execute('delete from tags;')
        self.cur.execute('delete from geotags;')
        self.cur.execute('delete from content;')
        self.cur.execute('delete from tagesschau;')
        self.conn.commit()

    def update_view(self):
        self.cur.execute('refresh materialized view public.index_retention;')
        self.conn.commit()

    def __insert_content(self, tagesschauId, contents):
        for index, content in enumerate(contents):
            self.cur.execute(f'''
                insert into content(
                    "tagesschauId",
                    "type",
                    "value",
                    "boxTitle",
                    "boxSubtitle",  
                    "boxText",
                    "boxLink",
                    "boxSource",
                    "videoSophoraId",
                    "videoExternalId",
                    "videoTitle",
                    "videoDate",
                    "videoUpdateCheckUrl",
                    "videoCopyright",
                    "videoType",
                    "videoAlttext",
                    "quotationText",
                    "webviewInline",
                    "htmlEmbedService",
                    "htmlEmbedUrl",
                    "audioDate",
                    "audioTeaserImageTitle",
                    "audioTeaserImageCopyright",
                    "audioTeaserImageAlttext",
                    "audioTeaserImageType",
                    "audioTitle",
                    "audioText",
                    "socialTitle",
                    "socialAccount",
                    "socialUsername",
                    "socialAvatar",
                    "socialUrl",
                    "socialShorttext",
                    "socialDate",
                    "index")
                values ({','.join(['%s' for x in range(35)])});
            ''', (
                tagesschauId,
                content['type'],
                content.get('value'),
                content.get('boxTitle'),
                content.get('boxSubtitle'),
                content.get('boxText'),
                content.get('boxLink'),
                content.get('boxSource'),
                content.get('videoSophoraId'),
                content.get('videoExternalId'),
                content.get('videoTitle'),
                content.get('videoDate'),
                content.get('videoUpdateCheckUrl'),
                content.get('videoCopyright'),
                content.get('videoType'),
                content.get('videoAlttext'),
                content.get('quotationText'),
                content.get('webviewInline'),
                content.get('htmlEmbedService'),
                content.get('htmlEmbedUrl'),
                content.get('audioDate'),
                content.get('audioTeaserImageTitle'),
                content.get('audioTeaserImageCopyright'),
                content.get('audioTeaserImageAlttext'),
                content.get('audioTeaserImageType'),
                content.get('audioTitle'),
                content.get('audioText'),
                content.get('socialTitle'),
                content.get('socialAccount'),
                content.get('socialUsername'),
                content.get('socialAvatar'),
                content.get('socialUrl'),
                content.get('socialShorttext'),
                content.get('socialDate'),
                index
            ))

    def __insert_geotags(self, tagesschauId, geotags):
        for index, geotag in enumerate(geotags):
            self.cur.execute('''
                insert into geotags(
                    "tagesschauId",
                    "tag",
                    "index")
                values (%s, %s, %s);
            ''', (
                tagesschauId,
                geotag['tag'],
                index
            ))

    def __insert_tags(self, tagesschauId, tags):
        for index, tag in enumerate(tags):
            self.cur.execute('''
                insert into tags(
                    "tagesschauId",
                    "tag",
                    "index")
                values (%s, %s, %s);
            ''', (
                tagesschauId,
                tag['tag'],
                index
            ))
