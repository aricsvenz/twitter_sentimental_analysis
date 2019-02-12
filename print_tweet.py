
import tweepy
from textblob import TextBlob
import csv #Import csv


consumer_key = 'CJ5WLkgAR2eI9IgaMp0TIXf5C'
consumer_secret = 'bsAmtZzcGtOIJgOigJ8iywPjFp7QkXPETXpujj0C488WeQEpgr'

access_token = '2514281718-OHA7jI2Qy1yBUuAD7PzcfE4GyhASrt8bJKo3iSr'
access_token_secret = 'zp0iFkIeCqWWI5EiPH2tgkDMKtmiC5CMERnyAiBBxRM86'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "country delight",
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()