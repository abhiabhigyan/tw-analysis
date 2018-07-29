# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:05:41 2018

@author: ABHIIGYAN SHIVAM
"""

import tweepy
import pandas as pd
import csv

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
consumer_key = "uG9mp726h5mB2t1uiUC6tZKSV"
consumer_secret = "tSVnIWPbjCdGlajukk8405Q1oz2TItCVWw4MntPEBVcNlSM8FF"
access_key = "1386381847-YprNKogpXFcBnIgpL8QPgyl9NilhTC2yFmGP3G5"
access_secret = "C12O3WQDWoGwewniLu1HXxFo6aztRoBq4aJoEoziG5PJn"

# Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets = 200
        tweets = api.user_timeline(screen_name=username,count=200)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        print(tmp)
        df = pd.DataFrame(tmp)
        df.to_csv("E:/archi_sem8/datasets/tweets/BDUTT.csv")

 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("@BDUTT") 
"""
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@narendramodi")"""
    
    
    