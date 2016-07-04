from twitter import *
import nltk
nltk.data.path.append('nltk_data')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json, pickle, os
from flask import jsonify

twitter = Twitter(auth = OAuth(os.environ['AccessToken'],
                               os.environ['AccessTokenSecret'],
                               os.environ['ConsumerKey'],
                               os.environ['ConsumerSecret']))

allowed_words = ['J']
stop_words = set(stopwords.words('english'))

word_features_file = open('classification/word_features.pickle','rb')
word_features = pickle.load(word_features_file)
word_features_file.close()

NBclassifier_file = open('classification/naive_bayes.pickle','rb')
NBclassifier = pickle.load(NBclassifier_file)
NBclassifier_file.close()


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

def tokenize(t):
    tokenized = word_tokenize(t['text'])
    trimmed = []
    for w in tokenized:
        if w not in stop_words:
            trimmed.append(w.lower())
    return trimmed

def prep_tweet(t):
    t['words'] = tokenize(t)
    t['features'] = find_features(t['words'])
    t['sentiment'] = NBclassifier.classify(t['features'])
    return t

def searchTweets(query):
    a = twitter.search.tweets(q = query)
    for t in a['statuses']:
        t = prep_tweet(t)
    return jsonify(a)
