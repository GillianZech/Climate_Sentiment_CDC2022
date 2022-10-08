import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
nltk.download('subjectivity')
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk import tokenize

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import csv

def analyze(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    return ss
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')

data = pd.read_csv(".csv")
data['score'] = data['text'].apply(analyze)
data.to_csv("frequencies")