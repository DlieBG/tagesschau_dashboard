from dotenv import load_dotenv, find_dotenv
from requests import post
from mongo import Mongo
from postgres import Postgres

load_dotenv(find_dotenv())

mongo = Mongo()
postgres = Postgres()

postgres.delete_articles()

for index, article in enumerate(mongo.get_articles()):
    postgres.insert_article(article)
    print(f"Progress: {int(index/mongo.get_articles_count()*100)}%\r", end='')