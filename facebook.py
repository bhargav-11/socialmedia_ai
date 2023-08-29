import requests
from dotenv import load_dotenv
import os

load_dotenv()
# Your Facebook Page Access Token
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

def post_to_facebook(payload):
    try:    
        page_id = os.getenv("FACEBOOK_PAGE_ID")
        url = f"https://graph.facebook.com/v17.0/{page_id}/feed"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {FACEBOOK_ACCESS_TOKEN}'
        }
        fb_payload = {
        "message": payload["post_message"]
        }
        response = requests.post(url, headers=headers, data=fb_payload)

        response_data = response.json()

        if response.status_code == 200:
            return {"message": "Successfully posted to Facebook"}  
        else:
            return {"error": "Failed to post to Facebook", "response": response_data}

    except requests.exceptions.RequestException as e:
        return {"error": "Request error occurred", "details": str(e)}, 500
    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}, 500