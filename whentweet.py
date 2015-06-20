import sys
sys.path.insert(0,'./..')
import twitter_oauth
import tweepy
import pandas as pd
from tweepy import API


auth = tweepy.OAuthHandler(twitter_oauth.CONSUMER_KEY, twitter_oauth.CONSUMER_SECRET)
auth.set_access_token(twitter_oauth.ACCESS_TOKEN, twitter_oauth.ACCESS_SECRET)

myapi = API(auth)

def getTweets(user):
	return tweepy.Cursor(myapi.user_timeline, id = user).items()
	

