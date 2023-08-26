from facebook import post_to_facebook
from linkedin import post_to_linkedin
from twitter import post_to_twitter
from flask import Flask, request, jsonify
import json
from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def create_payload(data):
    try:
        data_json = json.loads(data)
        text = data_json.get("message")
        image_url = data_json.get("imageurl")
        if not text:
            raise ValueError("Message is empty or missing in JSON data")
        
        payload = {
            "text": text,
            "imageurl": image_url
        }
        
        # Convert the payload dictionary to JSON
        payload_json = json.dumps(payload)
        
        return payload_json
    except Exception as e:
        return json.dumps({"error": str(e)})

@app.route('/facebook', methods=['POST'])
def facebook():
    data = request.data.decode('utf-8') 
    payload = create_payload(data)
    response = post_to_facebook(payload)
    return {"message" : "Successfully posted"} 

@app.route('/linkedin', methods=['POST'])
def linkedin_post():
    data = request.data.decode('utf-8')
    payload = create_payload(data)
    post_to_linkedin(payload)
    return "Success"

    # return {"message" : "Successfully posted"} 

@app.route('/twitter', methods=['POST'])
def twitter():
    data = request.data.decode('utf-8')
    payload = create_payload(data)
    response =  post_to_twitter(payload)
    return {"message" : "Successfully posted"} 

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
    

if __name__ == '__main__':
    app.run()