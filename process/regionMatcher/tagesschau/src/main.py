from dotenv import load_dotenv, find_dotenv
from postgres import Postgres
from regionMatcher import RegionMatcher

last_percent = ""

def print_percent(iteration, total, decimals = 0):
    global last_percent
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if percent != last_percent:
        print(percent + " %")
        last_percent = percent

load_dotenv(find_dotenv())

postgres = Postgres()
regionMatcher = RegionMatcher()
postgres.delete_clean_regions()

tagesschauIds = postgres.get_tagesschauIds()

for index, tagesschauId in enumerate(tagesschauIds):
    regionIds = postgres.get_regionIds(tagesschauId)
    dates = postgres.get_dates(tagesschauId)
    clean_region = regionMatcher.match(regionIds[0])
    postgres.insert_clean_region(tagesschauId, clean_region, dates[0])
    print_percent(index + 1, len(tagesschauIds))

postgres.commit()