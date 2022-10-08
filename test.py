import tweepy as tw
from secrets import API_KEY, SECRET_KEY, ACCESS_TOKEN, SECRET_TOKEN

auth = tw.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_TOKEN)
api = tw.API(auth, wait_on_rate_limit=True)

# Read IDs from .txt file and get tweets
ids = []
with open("climate_id.txt.00", 'r') as f:
    for _ in range(100):
        ids.append(f.readline()[:-1])

    tweets = api.lookup_statuses(ids)