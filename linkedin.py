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
    try:
        data = request.data.decode('utf-8')
        
        # if not data or "message" not in data:
        #     return jsonify({"error": "Invalid data. 'message' field is required."}), 400
        url = os.getenv("LINKEDIN_URL")
        linkedin_payload = json.dumps({
    "author": "urn:li:person:RbA3L6wq3T",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
        "shareCommentary": {
            # "text": payload["message"]
            "text": json.loads(data).get("generated_post")
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

        response = requests.post(url, data=linkedin_payload, headers=headers)
        response_data = response.json()

        if response.status_code == 201:
                return jsonify({"message": "Successfully posted to LinkedIn"}), 201
        else:
                return jsonify({"error": "Failed to post to LinkedIn", "response": response_data}), response.status_code

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

  

# if __name__ == '__main__':
#     app.run(debug=True)
