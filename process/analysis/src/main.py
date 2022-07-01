from dotenv import load_dotenv, find_dotenv
from postgres import Postgres
from textstrip import strip_tags
import spacy

last_percent = ""

def print_percent(iteration, total, decimals = 0):
    global last_percent
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if percent != last_percent:
        print(percent + " %")
        last_percent = percent

load_dotenv(find_dotenv())

tagesschau = Postgres()

tagesschau.delete_analysis()

nlp = spacy.load('de_core_news_sm')

#spacy.load('en_core_web_sm')

texts = tagesschau.getTexts()


for index, result in enumerate(texts):
    word_types = {'PRON':0, 'X':0, 'PROPN':0, 'SCONJ':0, 'PUNCT':0, 'NOUN':0, 'SPACE':0, 'INTJ':0, 'VERB':0, 'PART':0, 'AUX':0, 'NUM':0, 'CCONJ':0, 'DET':0, 'ADP':0, 'ADJ':0, 'ADV':0, 'SYM': 0}
    
    text = result[1]
    if text is None:
        continue
    text = strip_tags(text)
    analyis = nlp(text)
    for word in analyis:
        word_types[word.pos_] += 1
    
    tagesschau.insert_analyis(result[0], word_types)
    
    print_percent(index + 1, len(texts))

tagesschau.commit()