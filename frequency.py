import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
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
    # tokens = nltk.word_tokenize(list)
    f_dist = FreqDist(list)
    print(f_dist)
    f_dist.plot(20)
    return f_dist
full_list = []
def make_list_function(tweet):
    tokens = nltk.word_tokenize(tweet)
    for token in tokens:
        full_list.append(token)

data = pd.read_csv("nltk_split.csv").head(50)
data2 = pd.DataFrame(columns=["word", "frequency"])
data['text'].apply(make_list_function)
frequency_string = find_frequency(full_list).pformat(len(full_list))
# data2['frequency'] = find_frequency(full_list)
# data.to_csv("frequencies")
frequency_dict = ast.literal_eval(frequency_string[9:-1])
frequency_series = pd.Series(frequency_dict)
print(frequency_series)

# def count_words(list):
#     freq = {}
#     for word in list:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     return freq

# text = data['text'].tolist()
# text = [word_tokenize(x) for x in text]

# result = pd.Series(count_words(text))
# print(result)