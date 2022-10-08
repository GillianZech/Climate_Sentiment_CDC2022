import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd
import csv


def find_frequency(list):
    # tokens = nltk.word_tokenize(list)
    f_dist = FreqDist(list)
    print(f_dist)
    f_dist.plot()
    return f_dist
full_list = []
def make_list(tweet):
    tokens = nltk.word_tokenize(tweet)
    for token in tokens:
        full_list.append(token)

data = pd.read_csv("nltk_split.csv").head(5)
data2 = pd.DataFrame(columns=["word", "frequency"])
make_list = data['text'].apply(make_list)
data2['frequency'] = make_list(find_frequency)
# data.to_csv("frequencies")