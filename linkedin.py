from flask import Flask, request, jsonify
import requests,json
import os
from dotenv import load_dotenv

load_dotenv()
# Your LinkedIn API access token
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

# Post content to LinkedIn
# @app.route('/linkdin', methods=['POST'])
def post_to_linkedin(payload):
    url = os.getenv("LINKEDIN_URL")
    data = request.data.decode('utf-8')
    linkedin_payload = json.dumps({
    "author": "urn:li:person:RbA3L6wq3T",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
        "shareCommentary": {
            "text": json.loads(data).get("message")
            # "message": "hello"
        },
        "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
    })
    print("LinkedIn Payload:", payload)  
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}'
    
    }

    response = requests.request("POST", url, headers=headers,data=linkedin_payload)

    print(response.text)
    return {"message" : "Successfully posted"}

  

# if __name__ == '__main__':
#     app.run(debug=True)
