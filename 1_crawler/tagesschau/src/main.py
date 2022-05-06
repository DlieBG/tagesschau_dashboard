from dotenv import load_dotenv, find_dotenv
from insert_news import InsertNews
from update_news import UpdateNews
from time import sleep
import threading

load_dotenv(find_dotenv())

insert_news = threading.Thread(target=InsertNews)
insert_news.daemon = False
insert_news.start()

sleep(2 * 60)

update_news = threading.Thread(target=UpdateNews)
update_news.daemon = False
update_news.start()
