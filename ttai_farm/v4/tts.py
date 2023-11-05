import requests
from requests.exceptions import JSONDecodeError
from rich.progress import track
from mutagen.mp3 import MP3

# Fuction for Converting Text To Speech using SteamLabsPolly API (Voice is Set to 'Matthew')


def text_to_speach(text, filepath):
    body = {"voice": "Brian", "text": text, "service": "StreamElements"}
    response = requests.post(
        "https://lazypy.ro/tts/request_tts.php", data=body)
    # print(response.json())
    # try:
    voice_data = requests.get(response.json()["audio_url"])
    # print(voice_data)
    with open(filepath, "wb") as f:
        f.write(voice_data.content)
    # except (KeyError):
    #     print("Please Enter Text")
    # except (JSONDecodeError):
    #     print("Encountered an Error")
