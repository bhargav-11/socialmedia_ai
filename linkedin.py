import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Your LinkedIn API access token
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

# Post content to LinkedIn
def post_to_linkedin(payload):
    try:
        url = os.getenv("LINKEDIN_URL")
        linkedin_payload ={
        "author": "urn:li:person:RbA3L6wq3T",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
            "text": payload["post_message"]
            },
            "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
        }

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}'
        
        }

        response = requests.post(url, json=linkedin_payload, headers=headers)  
        response_data = response.json()
        print("response_data",response_data)
        if response_data.get("id"):
            return {"message": "Successfully posted to LinkedIn"}  
    
       
        return {"error": response_data["message"]}, 400
        
    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}, 500