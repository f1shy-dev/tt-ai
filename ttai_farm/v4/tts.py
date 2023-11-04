import requests
from requests.exceptions import JSONDecodeError
from rich.progress import track
from mutagen.mp3 import MP3

# Fuction for Converting Text To Speech using SteamLabsPolly API (Voice is Set to 'Matthew')


def text_to_speach(text, filepath):
    body = {"voice": "Matthew", "text": text, "service": "polly"}
    response = requests.post("https://streamlabs.com/polly/speak", data=body)
    try:
        voice_data = requests.get(response.json()["speak_url"])
        with open(filepath, "wb") as f:
            f.write(voice_data.content)
    except (KeyError):
        print("Please Enter Text")
    except (JSONDecodeError):
        print("Encountered an Error")
