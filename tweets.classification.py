# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:38:51 2018

@author: ABHIIGYAN SHIVAM
"""

import pandas as pd
import re
train = pd.read_csv('E:/archi_sem8/datasets/tweets/train1.csv')
#print(train.head())

def hyperlink(post):
  
  return (re.sub(r'https://.*','',post))

train['hyperlink'] = train['tweet'].apply(lambda x: hyperlink(x))
#print(train[['tweet','hyperlink']].head())

train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x.lower() for x in x.split()))
#print(train['hyperlink'].head())

train['hyperlink'] = train['hyperlink'].str.replace('[^\w\s]','')
#print(train['hyperlink'].head())

from nltk.corpus import stopwords
stop = stopwords.words('english')
train['hyperlink'] = train['hyperlink'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
#print(train['hyperlink'].head())

freq = pd.Series(' '.join(train['hyperlink']).split()).value_counts()[:10]
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
train['hyperlink'].apply(lambda x: str(TextBlob(x).correct()))
print(train['hyperlink'].head())