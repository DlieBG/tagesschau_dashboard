from dotenv import load_dotenv, find_dotenv
from postgres import Postgres
from cleaner import Cleaner

last_percent = ""

def print_percent(iteration, total, decimals = 0):
    global last_percent
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if percent != last_percent:
        print(percent + " %")
        last_percent = percent

load_dotenv(find_dotenv())

postgres = Postgres()
cleaner = Cleaner()

postgres.clean_regionId()

postgres.delete_clean_tags()

tagesschauIds = postgres.get_tagesschauIds()

for index, tagesschauId in enumerate(tagesschauIds):
    tags = postgres.get_tags(tagesschauId)
    clean_tags = [cleaner.clean(tag) for tag in tags]
    clean_tags = cleaner.unique(clean_tags)
    postgres.insert_clean_tags(tagesschauId, clean_tags)
    print_percent(index + 1, len(tagesschauIds))

print(cleaner.get_interesting_tags())

postgres.commit()