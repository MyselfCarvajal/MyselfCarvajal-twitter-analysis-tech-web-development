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

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# calling the api 
api = tweepy.API(auth)


keywords = ['#Javascript', '#Typescript']
limit = 300

# search tweets
public_tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode ='extended').items(limit)

# create dataframe
columns = ['User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('../searchHashtag.csv')

print(df)