from tweepy import Stream,OAuthHandler
from tweepy.streaming import StreamListener
import sqlite3
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode

analyzer = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey = "8Ze23elEqwdzQWVS0QzPsqi8B"
csecret = "oEQd2OjbFW4wW80EPqB26sKMO2yc4sRIgHn8uXOGCBtnXxB1aD"
atoken = "870570031368724482-y2FteP09SHuRdDDg40ji2MhtQdIUdLu"
asecret = "EpumJLFY3uTXsntJzfkAUq6vhz6aEamBJ6JeNvxrw1EIu"


#storing to db: sqlite3

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()


#Streaming Tweets
class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms,tweet, sentiment)
            c.execute("INSERT INTO sentiment(unix, tweet,sentiment) VALUES (?,?,?)",
            (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)

while True:
    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["a","e","i","o","u"])
    except Exception as e:
        print(str(e))
        time.sleep(5)
