import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret =os.getenv("access_token_secret")


def post_to_twitter(payload):
    try:
        if "post_message" not in payload:
            raise ValueError("Payload must contain 'post_message' key")

        tweet_text = payload["post_message"]
        tweet_text = tweet_text[:270]

        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        response = client.create_tweet(text=tweet_text)
       
        return {"message": "Successfully posted to Twitter", "tweet_id": response}
      

    except ValueError as ve:
        return {"error": "Failed to post to Twitter", "response_code": response.status_code}
       
    except tweepy.TweepyException as te:
        return {"error": f"Tweepy error: {str(te)}"}
