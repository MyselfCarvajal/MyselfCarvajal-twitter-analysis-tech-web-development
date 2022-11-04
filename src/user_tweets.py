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

# user tweets
user = 'elonmusk'
limit = 300

user_tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode ='extended').items(limit)

# create dataframe
columns = ['User', 'Tweet', 'Like', 'Retweet']
data = []

ucolumns = ['UserName', 'Name','UserDescription','Followers' , 'Following', 'Location']
udata= []

for tweet in user_tweets:
    data.append([tweet.user.screen_name, tweet.full_text, tweet.favorite_count, tweet.retweet_count])

udata.append([tweet.user.screen_name, tweet.user.name, tweet.user.description, tweet.user.followers_count, tweet.user.friends_count, tweet.user.location])

df = pd.DataFrame(data, columns=columns)
df.to_csv('../userTweets.csv')

Udf= pd.DataFrame(udata, columns=ucolumns)
Udf.to_csv('../elonData.csv')

print(df)