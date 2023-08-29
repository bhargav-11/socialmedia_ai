from facebook import post_to_facebook
from linkedin import post_to_linkedin
from twitter import post_to_twitter
from flask import Flask, request, jsonify
import json
from dotenv import load_dotenv
import os
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
def create_payload(data):
    try:
        data_json = json.loads(data)
        message = data_json.get("post_message")
        if not message:
            raise ValueError("Message is empty or missing in JSON data")

        payload = {
            "post_message": message,
        }

        return payload
    except Exception as e:
        return {"error": str(e)}

@app.route('/generate-post', methods=['POST'])
def generate_post():
    data = request.get_json()

    command = data.get('command')
    goal = data.get('goal')
    tone = data.get('tone')

    if not (command and goal and tone):
        return jsonify({'error': 'Missing required parameters'}), 400

    prompt = """
    Write a 500 words social media post based on below data points.

    command: {}
    goal: {}
    tone: {}
    """.format(command, goal, tone)

    response = openai.ChatCompletion.create(
              model="gpt-4-0613",
              messages=[{"role": "system", "content": 'You are a helpful assistant to create social media posts'},
                        {"role": "user", "content": prompt}
              ])
    
    post_content = response['choices'][0]['message']['content']

    response = {
        'generated_post': post_content
    }
    return jsonify(response)


@app.route('/post', methods=['POST'])
def post_to_social_media():
    data = request.data.decode('utf-8') # Assuming you're sending JSON data in the request body
    try:
        data_json = json.loads(data)  
    except json.JSONDecodeError:
        return {"error": "Invalid JSON payload"}
    platform = data_json.get('platform')  # Get the 'platform' field from the JSON data

    if not platform:
        return {"error": "Platform field is missing in the payload"}

    payload = create_payload(data)
    
    if platform == 'facebook':
        response = post_to_facebook(payload)
        return jsonify(response)
    elif platform == 'linkedin':
        response = post_to_linkedin(payload)
        return jsonify(response)
    elif platform == 'twitter':
        response = post_to_twitter(payload)
        return jsonify(response)
    else:
        return {"message": "Successfully posted to " + platform}

if __name__ == '__main__':
    app.run(debug=True)