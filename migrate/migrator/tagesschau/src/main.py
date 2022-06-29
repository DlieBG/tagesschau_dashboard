from dotenv import load_dotenv, find_dotenv
from mongo import Mongo
from postgres import Postgres

last_percent = ""

def print_percent(iteration, total, decimals = 0):
    global last_percent
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if percent != last_percent:
        print(percent + " %")
        last_percent = percent

load_dotenv(find_dotenv())

mongo = Mongo()
postgres = Postgres()

print('Altdaten werden gelöscht...', end = '\n')

postgres.delete_news()

length = mongo.get_count()

for index, news in enumerate(mongo.get_news()):
    postgres.insert_news(news)
    print_percent(index + 1, length, 1)

postgres.commit()
