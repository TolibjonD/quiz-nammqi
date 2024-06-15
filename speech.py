import requests
import json

API_KEY = "b1f40291-679c-4fb8-87c7-466794126457:6083f64d-f6ff-46b6-8879-9751ccbce4dd"

model = "fotima-neutral"

def tts(text,api_key=API_KEY, model=model):
    url = 'https://mohir.ai/api/v1/tts'
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'model': model,
        'blocking': "true",
        'webhook_notification_url': ""
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            return f"Request failed with status code {response.status_code}: {response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out. The API response took too long to arrive."

def get_audio(result):
    audio = result['result']['url']
    return audio