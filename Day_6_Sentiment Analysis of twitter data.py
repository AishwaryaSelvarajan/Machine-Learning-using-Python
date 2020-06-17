# API Keys and Token

API_key ='O0XTxcCz3TsMnl4BjNaY3y9n8'

API_secret_key = 'OvnS4HhntfGNooLsiPFhnRY9F1H31hDiMkTnEElUuCBDBCPlX3'

Access_Token = '842426903504011264-FV60xejeytG3HHH7sfbl6Xycj33fCzS'

Access_Token_Secret = '8cLup5zrGRBIIgu2eEteInsGJObKkGcawxXwM8NIujyFT'

import tweepy # Library for twitter API
from textblob import TextBlob # Another kind of Library for Sentiment Analysis, we can use NLTK library also

auth = tweepy.OAuthHandler(API_key, API_secret_key)

auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth) 

public_tweets = api.search('Narendra Modi')

print(public_tweets) # By default we will get 15 tweets

# To extract the text of the first tweet
public_tweets[0].text

# Sentiment Analysis of the first tweet using TextBlob
score = TextBlob(public_tweets[0].text)
print("The score of the first tweet is ")
print(score.sentiment)

# Here we have to see the polarity, which is similar to compound parameter in NLTK.

import pandas as pd 
data = pd.DataFrame()

# Extract the 15 tweets
tweets = []
for i in public_tweets:
    tweets.append(i.text)
data['Tweets'] = tweets
print(data)

# Calculating the score for 15 tweets
score = []
for i in public_tweets:
    s = (TextBlob(i.text)).sentiment
    score.append(s)
data['Sentiments'] = score
print(data)

metrics = []
for i in public_tweets:
    s = (TextBlob(i.text)).sentiment
    if s[0] > 0:
        metrics.append("Positive")
    elif s[0] < 0:
        metrics.append("Negative")
    else:
        metrics.append("Neutral")
data['Metric'] = metrics
print(data)
