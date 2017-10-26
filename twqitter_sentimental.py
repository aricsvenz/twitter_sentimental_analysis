import tweepy
from textblob import TextBlob

consumer_key = 'twitter_consumer_key'
consumer_secret = 'twitter_consumer_key_secret'

access_token = 'twitter_access_token'
access_token_secret = 'twitter_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


apt = tweepy.API(auth)

public_tweets = apt.search('xyz')

for tweet in public_tweets:
	print(tweet.text)
analysis = TextBlob(tweet.text)
print(analysis.sentiment)
