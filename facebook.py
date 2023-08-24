from flask import Flask, request, jsonify
import requests
import json
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
# Your Facebook Page Access Token
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
# @app.route('/facebook', methods=['POST'])
def post_to_facebook(payload):
    data = request.data.decode('utf-8')
    # print("DATA::", request.data)
    # print("DATA::", type(request.data))
    
    page_id = os.getenv("FACEBOOK_PAGE_ID")
    # page_id ="191914921205687"
    url = f"https://graph.facebook.com/v17.0/{page_id}/feed"

    # payload = json.dumps({
    # "message": json.loads(data).get("message")
    # })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {FACEBOOK_ACCESS_TOKEN}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return {"message" : "Successfully posted"}  # Optionally, you can return the response to the client

# if __name__ == '__main__':
#     app.run()
