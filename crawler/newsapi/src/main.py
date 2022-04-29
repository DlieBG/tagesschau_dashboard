from mongo import NewsApiMongoDB
from dotenv import load_dotenv, find_dotenv
from insert_news import InsertNews
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import json

load_dotenv(find_dotenv())

db = NewsApiMongoDB()
if not db.get_sources():
    sources = json.loads("sources.json")
    db.insert_sources(sources)

insert_news = InsertNews()

scheduler = BlockingScheduler()
scheduler.add_job(insert_news.crawl_news, 'interval', minutes=15, next_run_time=datetime.now())
scheduler.start()
