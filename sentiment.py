
import tweepy
from textblob import TextBlob

consumer_key = 'CJ5WLkgAR2eI9IgaMp0TIXf5C'
consumer_secret = 'bsAmtZzcGtOIJgOigJ8iywPjFp7QkXPETXpujj0C488WeQEpgr'

access_token = '2514281718-OHA7jI2Qy1yBUuAD7PzcfE4GyhASrt8bJKo3iSr'
access_token_secret = 'zp0iFkIeCqWWI5EiPH2tgkDMKtmiC5CMERnyAiBBxRM86'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


apt = tweepy.API(auth)

public_tweets = apt.search('patanjali milk')

for tweet in public_tweets:
	print(tweet.text)
analysis = TextBlob(tweet.text)
print(analysis.sentiment)