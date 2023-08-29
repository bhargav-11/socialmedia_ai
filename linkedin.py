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
        print("LinkedIn Payload:", payload)  
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}'
        
        }

        response = requests.post(url, json=linkedin_payload, headers=headers)  
        response_data = response.json()

        if response.status_code == 201:
            return {"message": "Successfully posted to LinkedIn"}  
        else:
            return {"error": "Failed to post to LinkedIn", "response": response_data}

    except requests.exceptions.RequestException as e:
        return {"error": "Request error occurred", "details": str(e)}, 500
    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}, 500