
import tweepy

consumer_key = "hDFZiGGk1Y2M4xYv57Tqv1fmZ"
consumer_secret = "39wJVJJe1jvrZG3NBDvE3XsaVsHNHqlkwgOC61oXdwozGjY02l"
access_token = "3168546722-8kXDPx67JEu8u3aKNIVvdKLPPOHA6kPkoJWh16i"
access_token_secret = "90yOFGaN0TbPeLY2oWyc4MtHTrAvPAWErZ9LrAuDl68RD"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


query = "modi"
language = "en"

results = api.search(q=query, lang=language)

for tweet in results:
    print(tweet)
    break
