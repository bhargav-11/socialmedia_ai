from facebook import post_to_facebook
from linkedin import post_to_linkedin
from twitter import post_to_twitter
from flask import Flask, request
import json
app = Flask(__name__)

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


    

if __name__ == '__main__':
    app.run()