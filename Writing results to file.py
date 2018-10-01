import csv
import xlwt
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier

from nltk.classify import ClassifierI
from statistics import mode
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from xlrd import open_workbook
import math
import re

import csv


print(nltk.__file__)

from tempfile import TemporaryFile
book = xlwt.Workbook()
for i in range(len(totalAccuracy)):
    sheet1 = book.add_sheet("sheets"+str(i+1))
    sheet1.write(0,1,"Accuracy")
    sheet1.write(0,2,"Positive Precision")
    sheet1.write(0,3,"Positive Recall")
    sheet1.write(0,4,"Negative Precision")
    sheet1.write(0,5,"Negative Recall")
    sheet1.write(0,6,"Positive F score")
    sheet1.write(0,7,"Negative F score")    
    for j in range(len(totalAccuracy[i])):
        sheet1.write(j+1,1,totalAccuracy[i][j][0])
        sheet1.write(j+1,2,totalAccuracy[i][j][1])
        sheet1.write(j+1,3,totalAccuracy[i][j][2])
        sheet1.write(j+1,4,totalAccuracy[i][j][3])
        sheet1.write(j+1,5,totalAccuracy[i][j][4])
        sheet1.write(j+1,6,totalAccuracy[i][j][5])
        sheet1.write(j+1,7,totalAccuracy[i][j][6])

name = "random.xls"
book.save(name)
book.save(TemporaryFile())



########### Sentiment analysis using Bag of words #############

#train = [("Great place to be when you are in Bangalore.", "pos"),
#  ("The place was being renovated when I visited so the seating was limited.", "neg"),
#  ("Loved the ambience, loved the food", "pos"),
#  ("The food is delicious but not over the top.", "neg"),
#  ("Service - Little slow, probably because too many people.", "neg"),
#  ("The place is not easy to locate", "neg"),
#  ("Mushroom fried rice was spicy", "pos"),
#]
#  
#
#
## Step 2
#dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
#  
## Step 3
#t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
#
## Step 4 – the classifier is trained with sample data
#classifier = nltk.NaiveBayesClassifier.train(t)
#  
#test_data = "Manchurian was hot and spicy"
#test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
#  
#print (classifier.classify(test_data_features))
#  