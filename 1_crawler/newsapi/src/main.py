from dotenv import load_dotenv, find_dotenv
from insert_news import InsertNews
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

load_dotenv(find_dotenv())

insert_news = InsertNews()

scheduler = BlockingScheduler()
scheduler.add_job(insert_news.crawl_news, 'interval', minutes=15, next_run_time=datetime.now())
scheduler.start()
