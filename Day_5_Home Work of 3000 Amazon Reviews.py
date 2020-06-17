# A .tsv file, which is a tab separated file has data of 3000 reviews from Amazon. The task is to categorise it as Positive and negative reviews and also to calculate the accuracy of the output

import pandas as pd 
dataframe = pd.read_csv('amazon_reviews.tsv',error_bad_lines = False, sep = '\t')
print(dataframe.head())

# Sentiment Analyser using Vader_lexicon
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

computed_score = []
for i in range(0,len(dataframe)):
    score = dataframe.iloc[:]['review']
    s = sia.polarity_scores(score)
    if (s['compound'] > 0):
        computed_score.append('Positive')
    elif (s['compound'] < 0):
        computed_score.append('Negative')
    else:
        computed_score.append("Neutral")
dataframe['Score'] = computed_score
print(dataframe.head())