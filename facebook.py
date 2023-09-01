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

        response_json = response.json()

        # Check for errors in the response JSON
        if "error" in response_json:
            error_message = response_json["error"]["message"]
            return {"error": f"Failed to post to Facebook: {error_message}", "response_code": response.status_code}
        
        # Check if the post was created successfully
        if response.status_code == 200:
            return {"message": "Successfully posted to Facebook", "post_id": response_json.get("id")}
        else:
            return {"error": "Failed to post to Facebook", "response_code": response.status_code}

    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}, 500