import re
import pandas as pd


# Clean tweet text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase and strip spaces
    return text


data="tweets.csv"
df = pd.DataFrame(data)

df['Cleaned Text'] = df['Text'].apply(clean_text)
df.to_csv('cleaned_tweets.csv', index=False)
print("Cleaned tweets saved to 'cleaned_tweets.csv'")

