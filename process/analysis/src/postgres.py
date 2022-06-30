import psycopg2
import os

translate = {
    'PRON': 'Pronomen',
    'X': 'Sonstiges',
    'PROPN': 'Eigenname',
    'SCONJ': 'unterordnende Konjunktion',
    'PUNCT': 'Satzzeichen',
    'NOUN': 'Nomen',
    'SPACE': 'Leerzeichen',
    'INTJ': 'Zwischenruf',
    'VERB': 'Verben',
    'PART': 'Partikel',
    'AUX': 'Hilfsverben',
    'NUM': 'Nummer',
    'CCONJ': 'nebenordnende Konjunktion',
    'DET': 'Artikel',
    'ADP': 'Präposition',
    'ADJ': 'Adjektiv',
    'ADV': 'Adverb',
    'SYM': 'Symbol'
}

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
    
    def delete_analysis(self):
        self.cur.execute('delete from content_analysis;')
        self.conn.commit()
    
    def insert_analyis(self, tagesschauId, analyis):
        for index, word_type in enumerate(analyis.keys()):
            self.cur.execute('''
                insert into content_analysis(
                    "tagesschauId",
                    "wordType",
                    "count"
                )
                values (%s, %s, %s);
            ''', (
                tagesschauId,
                translate[word_type],
                analyis[word_type]
            ))
        self.conn.commit()
    
    def commit(self):
        self.conn.commit()
