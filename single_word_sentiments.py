import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
nltk.download('subjectivity')
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk import tokenize

n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
# len(subj_docs), len(obj_docs) = 100
#Each document is represented by a tuple (sentence, label). The sentence is tokenized, so it is represented by a list of strings:

subj_docs[0]
# (['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one', 'thing', 'is', 'a', 'small', 'gem', '.'], 'subj')
#We separately split subjective and objective instances to keep a balanced uniform class distribution in both train and test sets.

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs
sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
#We use simple unigram word features, handling negation:

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
len(unigram_feats)
#83
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
#We apply features to obtain a feature-value representation of our datasets:

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)
#We can now train our classifier on the training set, and subsequently output the evaluation results:

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
#Training classifier
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import csv

def analyze(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    return ss


def classify(sentiment):
    if sentiment['neg'] == 1:
        return 'negative'
    elif sentiment['pos'] == 1:
        return 'positive'
    else:
        return 'neutral'

data = pd.read_csv("frequency.csv").rename(columns = {'Unnamed: 0': 'Word', '0': 'frequency'})
data['Word'] = data['Word'].astype(str)
data['sentiment'] = data['Word'].apply(analyze)
data['category'] = data['sentiment'].apply(classify)
positive = data[data['category'] == 'positive']
negative = data[data['category'] == 'negative']
neutral = data[data['category'] == 'neutral']
positive.to_csv("positive.csv")
negative.to_csv("negative.csv")
neutral.to_csv("neutral.csv")

sum_data = pd.read_excel("Sum.xlsx")
sum_data["sentiment"] = data['category']
sum_data.to_excel("Sum_data_classified.xlsx")