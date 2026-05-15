
import tweepy
import pandas as pd

# Twitter API credentials

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPxlwgEAAAAAyfI2wfR%2BW9qM0jziWDzZcGjvqOQ%3Dfq4qgSgm9wHuoyfBo3cQueWAoo1h3bjYATV5rVxwBQhzxIpzy5'
API_KEY = 'S8gMdAcBd8M5jYe0TBodXmJzd'
PI_SECRET = 'kBZIEFnbCPjYjDgYnRZ5PEXnEc3j1vZ52cbeTPXvmK2HWdRnEF'
CCESS_TOKEN = '1826634699248173056-GtwR8R50LdLdvKrhJcR1oW2QI63Vvc'
CCESS_TOKEN_SECRET = 'iBi6GgiqDmCw9WIygrHWeUYAC7cekQts6l8XKBz2iqB0k'
 #Authenticate with the API
client = tweepy.Client(bearer_token=BEARER_TOKEN)
 ##Search parameters
query = '(mental health OR anxiety OR depression) (social media) -is:retweet lang:en'
max_results = 100  # Number of tweets to fetch
 #Fetch tweets
response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text', 'created_at'])
# Store tweets in a DataFrame
tweets = []
for tweet in response.data:
    tweets.append({'Text': tweet.text, 'Created At': tweet.created_at})

df = pd.DataFrame(tweets)
df.to_csv('tweets2.csv', index=False)

print("Tweets saved to 'tweets.csv'")
import re

 #Clean tweet text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase and strip spaces
    return text
import pandas as pd
# Replace 'your_file.csv' with the path to your actual CSV file # Ensure you have pandas installed:
# pip install pandas
df = pd.read_csv('tweets.csv')
df['Cleaned Text'] = df['Text'].apply(clean_text)
df.to_csv('cleaned_tweets2.csv', index=False)

print("Cleaned tweets saved to 'cleaned_tweets2.csv'")