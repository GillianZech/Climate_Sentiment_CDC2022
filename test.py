import tweepy as tw
from itertools import zip_longest
import pandas as pd
from secrets import API_KEY, SECRET_KEY, ACCESS_TOKEN, SECRET_TOKEN

auth = tw.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_TOKEN)
api = tw.API(auth, wait_on_rate_limit=True)

# Groups ids into groups of 100 for the API
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

# data = pd.DataFrame(columns=["id", "text", 'favorite_count', 'retweet_count', 'created_at', 'coordinates'])
data = pd.read_csv("Dataset.csv")

# Read IDs from .txt file and get tweets
with open("climate_id.txt.03", 'r') as f:
    for lines in grouper(f, 25000, ''):
        ids = [x[:-1] for x in lines]
        ids = ids[::250]
        tweets = api.lookup_statuses(ids)
        for tweet in tweets:
            data = data.append({"id": tweet.id, 'text': tweet.text, 'favorite_count': tweet.favorite_count, 'retweet_count': tweet.retweet_count, 'created_at': tweet.created_at, 'coordinates': tweet.coordinates}, ignore_index=True)
        print(len(data))


data.to_csv("Dataset.csv")