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
        
        print("response_data",response.json())
        return {"message": "Successfully posted to Twitter"} , 200

    except Exception as ve:
        if len(ve.api_messages) > 0:
            return {"error": ve.api_messages[0]}, 400
        else:
         return {"error": "Fail to tweet"}, 400
       
