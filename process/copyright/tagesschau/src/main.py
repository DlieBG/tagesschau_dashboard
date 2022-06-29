from dotenv import load_dotenv, find_dotenv
from postgres import Postgres
from copyright import Copyright

last_percent = ""

def print_percent(iteration, total, decimals = 0):
    global last_percent
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if percent != last_percent:
        print(percent + " %")
        last_percent = percent

load_dotenv(find_dotenv())

postgres = Postgres()
copyright = Copyright()
postgres.delete_clean_copyright()

tagesschauEntries = postgres.get_tagesschauIds()

for index, tagesschauEntry in enumerate(tagesschauEntries):
    postgres.insert_clean_copyright(
        tagesschauEntry[0],
        copyright.get_copyright(tagesschauEntry[1])
    )

    print_percent(index + 1, len(tagesschauEntries))

postgres.commit()
