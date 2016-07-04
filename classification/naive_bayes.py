import nltk, pickle, time
from training_set import training_set

NBclassifier = nltk.NaiveBayesClassifier.train(training_set[:10000])
save = open('classification/naive_bayes.pickle','wb')
pickle.dump(NBclassifier, save)
save.close()