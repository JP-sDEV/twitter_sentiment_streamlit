import re
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

def parse_tweepy_response(tweepy_response):
    """
    Turns 'SearchResults' object from into a dictionary
    tweets_dictionary includes tweet's:
        - twitter handle(@username)
        - the tweet's text/content
        - date the tweet was posted

    Returns a diction
    """
    tweets_dictionary = {
    "twitter_name": [],
    "tweet_text": [],
    "date": [],
    "tweet_link": []
    }

    for r in tweepy_response:
        jsonified = r._json
        text = jsonified["text"]
        twitter_handle = jsonified["user"]["screen_name"]
        tweet_date = jsonified["created_at"]
        tweet_link = f"https://twitter.com/twitter/status/{jsonified['id']}"

        tweets_dictionary["twitter_name"].append(twitter_handle)
        tweets_dictionary["tweet_text"].append(text)
        tweets_dictionary["date"].append(tweet_date)
        tweets_dictionary["tweet_link"].append(tweet_link)

    return tweets_dictionary

def assign_sentiment_to_df(df):
    """
    Assign:
        - compound score (i.e. overall sentiment score)
        - postive sentiment (ratio in compound score)
        - neutral sentiment (ratio in compound score)
        - negatie sentiment (ratio in compound score)

    Returns a Pandas DataFrame
    """
    analyzer = SentimentIntensityAnalyzer()
    df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['tweet_text']]
    df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['tweet_text']]
    df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['tweet_text']]
    df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['tweet_text']]

    return df

def get_score_avgs(df, score_names):
    """
    Given a Pandas DataFrame and a list of score names (pos, neu, neg) return the averages of scores in the list

    Return Pandas DataFrame
    """
    avg_dict = {
        "score_name": score_names,
        "score_average": []
    }
    for name in score_names:
        avg_dict["score_average"].append(df[name].mean())

    avg_df = pd.DataFrame.from_dict(avg_dict)

    return avg_df

def clean_tweet(tweet):
    """
    Remove links, special characters (eg. @, #, etc.,) from a tweet

    Returns a str (string)
    """
    remove_special = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", tweet).split())).lower()
    stop_word_pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    cleaned = stop_word_pattern.sub('', remove_special) # removes stopwords
    
    return cleaned
