from dotenv import load_dotenv, find_dotenv
from postgres import Postgres
from textstrip import strip_tags
import spacy

def print_percent(iteration, total, decimals = 1):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    print(percent + " %")

load_dotenv(find_dotenv())

tagesschau = Postgres()

nlp = spacy.load('de_core_news_sm')

#spacy.load('en_core_web_sm')

texts = tagesschau.getTexts()

global_word_types = {'PRON':0, 'X':0, 'PROPN':0, 'SCONJ':0, 'PUNCT':0, 'NOUN':0, 'SPACE':0, 'INTJ':0, 'VERB':0, 'PART':0, 'AUX':0, 'NUM':0, 'CCONJ':0, 'DET':0, 'ADP':0, 'ADJ':0, 'ADV':0}

for index, result in enumerate(texts):
    word_types = {'PRON':0, 'X':0, 'PROPN':0, 'SCONJ':0, 'PUNCT':0, 'NOUN':0, 'SPACE':0, 'INTJ':0, 'VERB':0, 'PART':0, 'AUX':0, 'NUM':0, 'CCONJ':0, 'DET':0, 'ADP':0, 'ADJ':0, 'ADV':0}
    
    text = result[1]
    text = strip_tags(text)
    analisis = nlp(text)
    for word in analisis:
        word_types[word.pos_] += 1
    
    for key in global_word_types.keys():
        global_word_types[key] += word_types[key]
    print_percent(index + 1, len(texts))

print()
print(global_word_types)
print()
