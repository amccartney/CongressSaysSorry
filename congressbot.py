import tweepy, time, sys, os, ConfigParser

sys.path.append('keys-dir')

from key_file import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

filename = open('congress_screen_names.txt','r')
f = filename.readlines()
filename.close()

t = ['sorry',
    'apologize',
    'regret']

for a in f:
	a = a.rstrip()
	timeline = api.user_timeline(a)
	for status in timeline:
		x = status.text
		for i in t:
			if i in x:
				api.retweet(status.id)