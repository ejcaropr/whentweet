import sys
sys.path.insert(0,'./..')
import twitter_oauth
import tweepy
import pandas as pd
from tweepy import API
from datetime import timedelta as td
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

auth = tweepy.OAuthHandler(twitter_oauth.CONSUMER_KEY, twitter_oauth.CONSUMER_SECRET)
auth.set_access_token(twitter_oauth.ACCESS_TOKEN, twitter_oauth.ACCESS_SECRET)

myapi = API(auth)

def getTweets(user):
	return list(tweepy.Cursor(myapi.user_timeline, id = user).items())

class Wt:
	def __init__(self,user,limit=1000):
		self.cursor = tweepy.Cursor(myapi.user_timeline, id = user).items(limit)
		self.user = myapi.get_user(user)
		self.tweets = list(self.cursor)
		if self.user.utc_offset == None:
			self.offset = td()
		else:
			self.offset = td(seconds=self.user.utc_offset)

	def plot(self):
		t = [(t.created_at + self.offset).time() for t in self.tweets]
		d = [(t.created_at + self.offset).date() for t in self.tweets]
		colors = [ (t.created_at + self.offset).weekday() > 4 for t in self.tweets]

		plt.scatter(d,t,c = colors, alpha=0.5, s=100)
		plt.show()

