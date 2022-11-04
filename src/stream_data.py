import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('../config.init')

consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

bearer_token = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# calling the api 
api = tweepy.API(auth)

# Read tweets in real time
class MyStream(tweepy.StreamingClient):
    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected")
    
    def on_tweet(self, tweet):
       print(tweet.text) 
       #print(tweet.text) 
       return


stream = MyStream(bearer_token=bearer_token)
stream.add_rules(tweepy.StreamRule('#Javascript')) #adding the rules
stream.filter() #runs the stream
