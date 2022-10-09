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

for filename in ['climate_id.txt.00', 'climate_id.txt.01', 'climate_id.txt.02', 'climate_id.txt.03']:
    # Read IDs from .txt file and get tweets
    with open(filename, 'r') as f:
        f.readline() # To ensure no duplicate IDs are used

        # Only read every 200th tweet
        for lines in grouper(f, 20000, ''):
            ids = [x[:-1] for x in lines]
            ids = ids[::200]
            tweets = api.lookup_statuses(ids)
            for tweet in tweets:
                data = pd.concat([data, pd.Series({"id": tweet.id, 'text': tweet.text, 'favorite_count': tweet.favorite_count, 'retweet_count': tweet.retweet_count, 'created_at': tweet.created_at, 'coordinates': tweet.coordinates})], ignore_index=True)
            print(len(data))
        
    print(f'{filename} done')


data.to_csv("Dataset.csv")