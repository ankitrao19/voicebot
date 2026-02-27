import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CARTESIA_API_KEY")

url = "https://api.cartesia.ai/voices/clone"

files = {"clip": ("recordings/voice1.mp3", open("recordings/voice1.mp3", "rb"))}
payload = {
    "name": "church voice",
    "description": "test 1",
    "language": "en",
    "base_voice_id": "<string>"
}
headers = {
    "Cartesia-Version": "2025-04-16",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)
