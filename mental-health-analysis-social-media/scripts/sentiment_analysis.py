from textblob import TextBlob
import pandas as pd

# Load your dataset
data = pd.read_csv('cleaned_tweets2.csv')

# Apply TextBlob sentiment analysis
def get_sentiment_textblob(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

data['Sentiment_TextBlob'] = data['text'].apply(get_sentiment_textblob)
data.to_csv('/mnt/data/sentimentt_textblob2.csv', index=False)
print("Sentiment analysis with TextBlob complete!")
