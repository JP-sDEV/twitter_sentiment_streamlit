import os
import tweepy
import pandas as pd
from helper_functions import assign_sentiment_to_df, parse_tweepy_response, clean_tweet

CONSUMER_KEY = os.environ.get("TWITTER_API_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET
    )

auth.set_access_token(
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
    )

api = tweepy.API(auth)

def query_tweets(hashtag, count=100, lang="en", result_type="popular"):
    """
    Get 100 Tweets containing the hashtag
    Ignores retweets with hashtag

    Returns a 'SearchResults' object
    """
    results = api.search_tweets(
        q=f"{hashtag} -filter:retweets", 
        count=count,
        lang = lang,
        result_type = result_type,
        geo="43.6532 79.383 15km" # Toronto lat, long
        )

    parse_results = parse_tweepy_response(results)

    return parse_results

def results_to_df(results):
    """
    Turns the 'SearchResults' Object (from the Twitter API) into a Pandas DataFrame
    Turns the string date into a valid Pandas datetime type

    Returns a Pandas DataFrame
    """
    tweets_df = pd.DataFrame.from_dict(data = results)
    tweets_df["date"] = pd.to_datetime(tweets_df["date"])
    sentiment_df = assign_sentiment_to_df(tweets_df)
    sentiment_df["tweet_text"] = sentiment_df["tweet_text"].apply(clean_tweet) 

    return sentiment_df
