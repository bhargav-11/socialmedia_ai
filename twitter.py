from flask import Flask, request, jsonify
import tweepy,requests,json
import os
from dotenv import load_dotenv
import random
import time
import hashlib
load_dotenv()


# Twitter API credentials
oauth_consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
oauth_token = os.getenv("access_token")
access_token_secret =os.getenv("access_token_secret")
oauth_callback= os.getenv("oauth_callback")
# Initialize Tweepy with API credentials
auth = tweepy.OAuthHandler(oauth_consumer_key, consumer_secret)
auth.set_access_token(oauth_token, access_token_secret)
api = tweepy.API(auth)

# @app.route('/twitter', methods=['POST'])
def post_to_twitter(payload):
    data = request.data.decode('utf-8')
    print("DATA::", request.data)
    print("DATA::", type(request.data))
    url = os.getenv("TWITTER_URL")

    # payload = json.dumps({
    # "text": json.loads(data).get("message")
    # })
  
    headers = {
                'Content-Type': 'application/json',
        'Authorization': 'OAuth oauth_consumer_key="xZpBoXHFykVkJoBnetogpy12F",oauth_token="1692152164674629632-FwTSaKjdYsAubXEGj2IRJSRTVBtNdK",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1692876997",oauth_nonce="NX8MfrGlirb",oauth_version="1.0",oauth_body_hash="XSWk1lAQos1%2FLnojme%2Fn7PNdpUw%3D",oauth_callback="https%3A%2F%2F2e82-2401-4900-1f3e-7682-c2ce-4d56-e190-738b.ngrok-free.app",oauth_signature="Ri1McWuXeX%2Flmxg4h6P882scF6k%3D"',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return {"message" : "Successfully posted"}
