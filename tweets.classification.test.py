# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:38:51 2018

@author: ABHIIGYAN SHIVAM
"""

import pandas as pd
import re

train2 = pd.read_csv('E:/archi_sem8/datasets/tweets/train2.csv')
test2 = pd.read_csv('E:/archi_sem8/datasets/tweets/test2.csv')

#print(test2.head())

import csv
with open('E:/archi_sem8/datasets/tweets/train3.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]


with open('E:/archi_sem8/datasets/tweets/test3.csv') as e:
    data2=[tuple(line) for line in csv.reader(e)]    


#print(data)
#print(train2.head())



from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(data)

print(cl.classify('maoists city police crackdown suspected maoists pune uncovers assassination threats c'))

print(cl.accuracy(data2))

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob("I like the cow slaughters and thier supportes ", analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)










