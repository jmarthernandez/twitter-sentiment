from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random, pickle, nltk

# Read Training Data
short_pos = open('classification/positive.txt', 'r', encoding='utf-8', errors='replace').read()
short_neg = open('classification/negative.txt', 'r', encoding='utf-8', errors='replace').read()

documents = []
all_words = []
allowed_words = set(['J'])
stop_words = set(stopwords.words('english'))

for r in short_pos.split('\n'):
  documents.append((r, 'pos'))
  words = word_tokenize(r)
  pos = nltk.pos_tag(words)
  for w in pos:
    if w[1][0] in allowed_words and w[1][1] not in stop_words:
        all_words.append(w[0].lower())

for r in short_neg.split('\n'):
  documents.append((r, 'neg'))
  words = word_tokenize(r)
  pos = nltk.pos_tag(words)
  for w in pos:
    if w[1][0] in allowed_words and w[1][1] not in stop_words:
        all_words.append(w[0].lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:5000]

save = open('classification/word_features.pickle','wb')
pickle.dump(word_features, save)
save.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

training_set = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(training_set)
