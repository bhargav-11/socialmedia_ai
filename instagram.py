from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Instagram Business Account Access Token
ACCESS_TOKEN = "EAACPHabsi3oBO5ZCFipYwSMEyXRQZBt9JDm50YNzDmlU6srmnCJAyaaFNHZAqrJoSZBs7z7WBoYBcYqUZBdXm9wJkclgp7VYjQsfxYTE6fbEOcYbAZBmsH3ffQHXC8Q8oPur6oN2ZByinGLHGDZBg4RAyLly3zQ1X6yFGHOlTEw4UyZB0eAQ8qalhkySuNZAO6WFHd7ylVUdgwvyQ8u19m17oWgxTExHBIBDt740wY"

@app.route('/post_to_instagram', methods=['POST'])
def post_to_instagram():
    try:    
        data = request.get_json()

        caption = data.get('caption', '')  # Caption for the post
        image_url = data.get('image_url', '')  # URL of the image to be posted

        # Create the API endpoint URL
        url = f'https://graph.instagram.com/me/media'

        # Prepare the payload
        payload = {
            'access_token': ACCESS_TOKEN,
            'caption': caption,
            'image_url': image_url,
            'media_type': 'IMAGE'
        }

        # Make the POST request to Instagram Graph API
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Post successful'})
        else:
            return jsonify({'success': False, 'message': 'Failed to post'})

    except Exception as e:
        return jsonify({'success': False, 'message': 'Error: ' + str(e)})

if __name__ == '__main__':
    app.run()
