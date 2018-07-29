# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:06:41 2018

@author: ABHIIGYAN SHIVAM
"""

import pandas as pd
import re
train = pd.read_csv('E:/archi_sem8/datasets/tweets/master.csv')
#print(train.head())
train['word_count'] = train['tweet'].apply(lambda x: len(str(x).split(" ")))
#print(train[['tweet','word_count']].head())

from nltk.corpus import stopwords
stop = stopwords.words('english')
train['stopwords'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x in stop]))
#print(train[['tweet','stopwords']].head())

def hyperlink(post):
  
  return (re.sub(r'https://.*','',post))

train['hyperlink'] = train['tweet'].apply(lambda x: hyperlink(x))
#print(train[['tweet','hyperlink']].head())
"""train.to_csv("E:/archi_sem8/datasets/tweets/te.csv")"""

train['numerics'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
#print(train[['tweet','numerics']].head())

#Cleaning from here

train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x.lower() for x in x.split()))
#print(train['hyperlink'].head())

train['hyperlink'] = train['hyperlink'].str.replace('[^\w\s]','')
#print(train['hyperlink'].head())

train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
#print(train['hyperlink'].head())

freq = pd.Series(' '.join(train['hyperlink']).split()).value_counts()[:15]
#print(freq)

freq = list(freq.index)
train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
#print(train['hyperlink'].head())

freq2 = pd.Series(' '.join(train['hyperlink']).split()).value_counts()[-30:]
#print(freq2)

freq2 = list(freq2.index)
train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x for x in x.split() if x not in freq2))
#print(train['tweet'].head())

from textblob import TextBlob
#train['hyperlink'].apply(lambda x: str(TextBlob(x).correct()))
#print(train['hyperlink'].head())



from textblob import Word
train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
#print(train['hyperlink'].head())

tf1 = (train['hyperlink'][1:1300]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
tf1.columns = ['words','tf']
#print(tf1)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',
 stop_words= 'english',ngram_range=(1,1))
train_vect = tfidf.fit_transform(train['tweet'])
#print(train_vect)

from sklearn.feature_extraction.text import CountVectorizer
bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")
train_bow = bow.fit_transform(train['hyperlink'])
#print(train_bow)

#print(train['hyperlink'][:100].apply(lambda x: TextBlob(x).sentiment))

train['sentiment'] = train['hyperlink'].apply(lambda x: TextBlob(x).sentiment[0] )
print(train[['hyperlink','sentiment']])





















