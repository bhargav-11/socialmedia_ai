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
    try:    
        data = request.data.decode('utf-8')
        payload = json.loads(data)
        page_id = os.getenv("FACEBOOK_PAGE_ID")
        url = f"https://graph.facebook.com/v17.0/{page_id}/feed"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {FACEBOOK_ACCESS_TOKEN}'
        }
    

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        if response.status_code == 200:
            return {"message": "Successfully posted to Facebook"}, 200
        else:
            return {"error": "Failed to post to Facebook", "response": response_data}, response.status_code

    except requests.exceptions.RequestException as e:
        return {"error": "Request error occurred", "details": str(e)}, 500
    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}, 500

   