from nltk.classify.scikitlearn import SklearnClassifier
import pickle
import random

from nltk.corpus import stopwords

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


ps = PorterStemmer()
punctuations = ["'","!","(",")","-","[","]","{","}",";",":",",","<",">",".","/","?","@","#","$","%","^","&","*","_","~","\""]
word_split_data = []

stopWords = set(stopwords.words('english'))
conjunctions = ['for','and','nor','but','or','yet','so','']
conjunctions2= ' and | nor | but | or | yet | so |\[comma\] |; '




def wordstemming(word):
    return ps.stem(word)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# define punctuation
def punctuation_remove(word):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuation from the string
    no_punct = ""
    for char in word:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct





#wb = open_workbook(r'C:\Users\Ashwin PC\Desktop\MS Materials\Data Mining and text mining\Project - 2\training-Obama-Romney-tweets.xlsx')
#wb = open_workbook(r'C:\Users\M.PANT\Desktop\UIC MSCS\Spring2018\CS583-DMTM\Project2\dara 1_train.csv')

recordList= []
with open('C:\\Users\\abhis\\Desktop\\UIC Subjects\\DMTM\\Project 2\\dara 1_train.csv') as csvFile:
#with open('C:\\Users\\M.PANT\\Desktop\\UIC MSCS\\Spring2018\\CS583-DMTM\\Project2\\data 2_train.csv') as csvFile:
    readCSV= csv.reader(csvFile, delimiter=',' )
    for row in readCSV:
        recordList.append(row)


recordList.pop(0) # removing the example,tweet,aspect_word,location, label row

#making aspect_terms list
aspect_words=[]
recordsDict={}
record=[]


for rowitem in recordList:
    aspect_words.append(rowitem[2])


for rowitem in recordList:       
    tweet = rowitem[1]
    class_label = int(rowitem[4] )
    if class_label in [-1,0,1]:
        #if rowitem[2] not in recordsDict.keys():
        #    recordsDict[rowitem[2]]=[]            
        #recordsDict[ rowitem[2] ].append([tweet,class_label])
        record.append([tweet,class_label])



neoRecord=[]
for rowitem in recordList:
    tweet= rowitem[1]
    aspect= rowitem[2]
    class_label = int(rowitem[4] )
    aspect_index= rowitem[3].split('--')
    indexRange=[ int(s) for s in aspect_index ]
    neoTweet=""
    neoTweetList= re.split(conjunctions2 , tweet)
    for subSentence in neoTweetList:
        if aspect in subSentence:
            neoTweet=subSentence
    
    if class_label in [-1,0,1]:
        neoRecord.append([neoTweet,class_label])      
            
    

    

#aspect_words=list( set(aspect_words) )

#print(aspect_words[0])



records = []




#obama = wb.sheet_by_name("Romney")
#for row in range(2, obama.nrows):
#    tweet = obama.cell(row, 3).value
#    class_value = obama.cell(row, 4).value
#    if class_value in [-1, 0, 1]:
#        records.append([tweet, class_value])



records = neoRecord#record #recordsDict['human interface']

#Abhishek CHANGE#########3
#   
#allowdWordsTypesPOS=['JJ', 'JJR', 'JJS','VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ','RB', 'RBR', 'RBS']
allowedPOS=['J','V','R']
    

allWords=[]
tokenizedSentence=[]

tweetWords2=[]
   
    ####################
    #remove Stop words #
    ###Abhishek Change####
    #for w in tweet_words:
    #    if w not in stopWords:
    #        tweetWords2.append(w)
#            
    #tweet_words=tweetWords2

for sentence in records:
    tokenizedSentence = word_tokenize(sentence[0]) #[1] has label
    
    for item in tokenizedSentence:
        if item in stopWords:
            tokenizedSentence.remove(item)
    
    posTagged= nltk.pos_tag(tokenizedSentence)
    for word in posTagged:
        if word[1][0] in allowedPOS:
            allWords.append(word[0].lower())
    
    
    
allWords = nltk.FreqDist(allWords)
word_features = list(allWords.keys())[:1000]


#CREATE DICTIONARY
def find_features(subSentence):
    words = word_tokenize(subSentence)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#
    
############# Abhishek Change########
featuresets = [ [find_features(subSentence), label] for [subSentence, label] in records ]

random.shuffle(featuresets)
print(len(featuresets))
records=featuresets
####################################





print(len(records))



# n-cross validation
n = 10
split = len(records)/n




def split_record(i, split):
    if math.ceil(i/split) == 0:
        return 1
    else:
        return math.ceil(i/split)







total_records = []
vocabulary = []
for i in range(len(records)):
    total_records.append([records[i], split_record(i, split)])
#print(total_records[0:100])
#vocabulary = 
    
    
    
    
def tweet_split(tweet):
    tweet_dict = {}
    tweet_set = {}
    cleantweet = cleanhtml(tweet)
    tweet_words = [wordstemming(word) for word in word_tokenize(cleantweet) if wordstemming(word) not in stopwords.words('english') and wordstemming(word) not in punctuations]
    
    #tweet_words= [word for word in word_tokenize(cleantweet) ] #Abhishek Change
    
    #print(word_tokenize(cleantweet))
    #print(tweet_words)
    tweetWords2=[]
   
    ####################
    #remove Stop words #
    ###Abhishek Change####
    #for w in tweet_words:
    #    if w not in stopWords:
    #        tweetWords2.append(w)
#            
    #tweet_words=tweetWords2
    ###################
    
    tagged = nltk.pos_tag(tweet_words)
    #print(tagged)
        
            
    i = 0
    adjectiveCount=0
    verbCount = 0
    adverbCount = 0
    i = 0
    for word in set(tagged):
        tweet_dict[str(word[0]) + "pos tag"] = word[1]
        tweet_dict[str(word[0]) + "exists"] = True
        i+=1
    for word in set(tagged):
        if word[1] in ('JJ', 'JJR', 'JJS'): 
            if adjectiveCount <= 2:
                tweet_dict['adj'+str(adjectiveCount)] = str(word[0])
                adjectiveCount+=1
        if word[1] in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            if verbCount <= 4:
                tweet_dict['verb'+str(verbCount)] = str(word[0])
                verbCount+=1
        if word[1] in ('RB', 'RBR', 'RBS'):
            if adverbCount <= 4:
                tweet_dict['adverb'+str(adverbCount)] = str(word[0])
                adverbCount+=1
        i+=1
    for j in range(adjectiveCount,3):
        tweet_dict['adj'+str(adjectiveCount)] = 'False'
        adjectiveCount+=1
    for j in range(verbCount,5):
        tweet_dict['verb'+str(verbCount)] = 'False'
        verbCount+=1
    for j in range(adverbCount,5):
        tweet_dict['adverb'+str(adverbCount)] = 'False'
        adverbCount+=1
    return tweet_dict



def subSentenceSplit(subsentence):
    featureDict = find_features(subsentence)#[ [find_features(subSentence), label] for [subSentence, label] in records ]
    return featureDict
    #random.shuffle(featuresets)
    #print(len(featuresets))
    #records=featuresets


def featureSelection(training_data):
    print("---- In feature Selection")
    word_split_data = []
    for record in training_data:
        #print(record)
        #print([tweet_split(record[0]),record[1]])
        if record[1] in [0, 1, -1]:
            #word_split_data.append([tweet_split(record[0]),record[1]])
            ###Abhishek Change######
            word_split_data.append([subSentenceSplit(record[0]),record[1]])
            ##########
    return [word_split_data]








import csv
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()    
accuracyResults = []
classifierAccuracy = []
totalClassifiers = []
crossValidationData = []
for i in range(1,11):
    print("----Loop "+ str(i))
    training_data = []
    test_data = []
    for record in total_records:
        if record[1] == i:
            test_data.append(record[0])
        else:
            training_data.append(record[0])
    #crossValidationData.append([featureSelection(training_data), test_data])
    ###########Abhishek Change###########
    crossValidationData.append([training_data, test_data])
    print(" ------- Classifier "+str(i))
    #print(classifier)