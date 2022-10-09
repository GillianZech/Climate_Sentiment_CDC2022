import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
nltk.download('punkt')
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

def analyze(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    return ss

data = pd.read_csv("Dataset.csv")
data['score'] = data['text'].apply(analyze)
data['neg'] = data['score'].apply(lambda x: x.get('neg'))
data['neu'] = data['score'].apply(lambda x: x.get('neu'))
data['pos'] = data['score'].apply(lambda x: x.get('pos'))
data['compound'] = data['score'].apply(lambda x: x.get('compound'))
data.to_csv("nltk_data.csv")