import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.probability import ConditionalFreqDist
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
    # for word in list:
    #     condition = word.isalnum()
    #     f_dist[condition][word] += 1
    print(f_dist)
    # to_return = f_dist.r_Nr()
    f_dist.plot()
    return f_dist #to_return
full_list = []
def make_list_function(tweet):
    tokens = nltk.word_tokenize(tweet)
    for token in tokens:
        full_list.append(token)

data = pd.read_csv("nltk_split.csv")
data2 = pd.DataFrame(columns=["word", "frequency"])
data['text'].apply(make_list_function)
# print(find_frequency(full_list))
frequency_string = find_frequency(full_list).pformat(len(full_list))
# data2['frequency'] = find_frequency(full_list)
# data.to_csv("frequencies")
frequency_dict = ast.literal_eval(frequency_string[9:-1])
frequency_series = pd.Series(frequency_dict)
frequency_series = frequency_series[frequency_series.index.str.isalnum()]
frequency_series = frequency_series.drop(labels=['RT'])
print(frequency_series)
frequency_series.to_csv("frequency.csv")

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