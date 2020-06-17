# The Library we are going to use is NLTK - Natural Language Toolkit
# The package inside NLTK is Vader -Lexicon, created by Facebook for Sentiment Analysis

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# An example - SupposeI give a review as good, lets see what the Sentiment Intensity Analyser does
review1 = 'good'
review = sia.polarity_scores(review1)
print (review)

# The compound value of the review matters here. If the compound value is > 0, then it is positive, if near to 1, then the review is more positive
# If the compound value is < 0, then it is negative, if near to -1, then the review is more negative

# Lets take the previous example of amazon product
import pandas as pd 
data = pd.read_csv('Amazon_reviews.csv')
print (data)

score = []

for i in range(0,len(data)):
    review = data.iloc[i]['Review']
    s = sia.polarity_scores(review)
    if (s['compound'] > 0):
        score.append('Positive')
    elif (s['compound'] < 0):
        score.append('Negative')
    else:
        score.append("Neutral")
data['Score'] = score
print(data)

