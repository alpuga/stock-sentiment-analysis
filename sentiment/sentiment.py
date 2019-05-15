# import twitter keys and tokens
from config import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy

import json
from textblob import TextBlob
import time
from elasticsearch import Elasticsearch

time.sleep(12)

# create instance of elasticsearch
es = Elasticsearch([{"host": "elasticsearch", "port": "9200"}])


class TweetStreamListener(tweepy.StreamListener):

    # on success
    def on_data(self, raw_data):
        self.process_data(raw_data)

        return True

    def process_data(self, raw_data):
        # Decode json
        tweet_data = json.loads(raw_data)
        print(tweet_data["text"])

        # Pass tweet into TextBlob
        tweet = TextBlob(tweet_data["text"])

        # Output sentiment polarity
        print(tweet.sentiment.polarity)

        # Positive, Negative, or Neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "Negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        # print sentiment
        print(sentiment)

        # add text and sentiment info to elasticsearch db
        es.index(index="sentiment",
                 doc_type="tweet",
                 body={"author": tweet_data["user"]["screen_name"],
                       "date": tweet_data["created_at"],
                       "message": tweet_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})

    # on failure
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


# Create a stream
class TweetStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)


# Start stream
if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = TweetStream(auth, listener)

    # search twitter for keyword(s)
    stream.start(['$TSLA', 'Tesla'])
