from keys import keys

import tweepy, time, sys, os, ConfigParser

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

filename = open('congress_screen_names.txt','r')
f = filename.readlines()
filename.close()

twts = api.search(q="sorry")


t = ['sorry',
    'apologize',
    'regret']

for a in f:
	api.user_timeline([a])
	for s in twt:
	    for i in t:
	        if i == s.text:
	            r = api.retweet(s.id)
	            time.sleep(1800)
	        else:
	        	time.sleep(1800)


