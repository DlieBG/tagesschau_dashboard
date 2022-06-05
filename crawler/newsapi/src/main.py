from mongo import NewsApiMongoDB
from dotenv import load_dotenv, find_dotenv
from insert_news import InsertNews
from insert_historic_news import InsertHistoricNews
from process_errors import ProcessErrors
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import json

load_dotenv(find_dotenv())

db = NewsApiMongoDB()
if not db.get_sources():
    f = open("sources.json")
    sources = json.loads(f.read())
    f.close()
    db.insert_sources(sources)
start = datetime.now()

insert_news = InsertNews()
process_errors = ProcessErrors()
historic_news = InsertHistoricNews(start - timedelta(days = 1))

scheduler = BlockingScheduler()
scheduler.add_job(insert_news.crawl_news, 'interval', minutes=15, next_run_time=start)
scheduler.add_job(historic_news.crawl_historic_news, 'interval', days=1, next_run_time=start)
scheduler.add_job(process_errors.process_errors, 'interval', days=1, next_run_time=start)
scheduler.start()
scheduler.join()