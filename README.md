# Stock Sentiment Analysis

> Analyzing sentiment on particular stocks on Twitter.
> The specific example I used was Tesla.
> Could be used for sentiment analysis on any particular topic, I used it for stocks.

## Configuration

In order to access the Twitter API, you need to register the application with Twitter.
After you register, you will receive consumer secret & key. Also, under "Keys and Access Tokens", create an access token & token secret. Add them to a new file config.py.

`./sentiment/config.py`

```
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

## Quick Start

```bash
$ docker-compose up
```

## Built With

This project uses the following technologies:

- [Docker](https://www.docker.com/) for microservice containerization.
- [Elasticsearch](https://www.elastic.co/products/elasticsearch) for storing tweet data.
- [Kibana](https://www.elastic.co/products/kibana) for visualizing data.
- [Twitter API](https://developer.twitter.com/en/docs) to access tweets.
- [Tweepy](http://www.tweepy.org/) a python library to access the Twitter API.
- [TextBlob](https://textblob.readthedocs.io/en/dev/) for processing textual data using NLP for the sentiment.

## App Info

### Version

1.0.0

### License

This project is licensed under the MIT License
