import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.probability import ConditionalFreqDist
from nltk.corpus import stopwords, words
import pandas as pd
import csv
import sqlite3
import json
import ast

# conn = sqlite3.connect('nltk_split.csv')
# cursor = conn.cursor()
# cursor.execute('PRAGMA foreign_keys = ON')

# # import comp421
# # check, report = comp421.start('A2')

# query = """select """

# # test code
# ex = cursor.execute(query).fetchone()[0]
# print(f'')


def find_frequency(list):
    f_dist = FreqDist(list)
    # f_dist.plot()
    return f_dist 
full_list = []
def make_list_function(tweet):
    tokens = nltk.word_tokenize(tweet)
    for token in tokens:
        full_list.append(token.lower())

data = pd.read_csv("nltk_split.csv")
data2 = pd.DataFrame(columns=["word", "frequency"])
data['text'].apply(make_list_function)
frequency_string = find_frequency(full_list).pformat(len(full_list))
frequency_dict = ast.literal_eval(frequency_string[9:-1])
frequency_series = pd.Series(frequency_dict)
frequency_series = frequency_series[frequency_series.index.str.isalnum()]
frequency_series = frequency_series[~frequency_series.index.str.lower().isin(stopwords.words('english'))]
frequency_series = frequency_series[frequency_series.index.str.lower().isin(words.words())]
print(frequency_series)
frequency_series.to_csv("frequency.csv")
