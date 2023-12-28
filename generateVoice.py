import requests
import os


def narrate(script, filename, voice):

    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "YOUR_API_KEY"
    }

    data = {
        "text": script,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open(f'{filename}.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

content = """ """

voices = {
    "Antoni" : "ErXwobaYiN019PkySvjV",
    "Rachel" : "21m00Tcm4TlvDq8ikWAM",
}

voice = voices["Antoni"]

narrate(content, "output", voice)
