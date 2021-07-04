import os
import json
import time
import random
import string
import pyttsx3
import requests
import speech_recognition as sr
from gtts import gTTS
from flask import Flask, request

DEFAULT_FILE_SPEAk = "audio/speak/{}-{}.wav"
app = Flask(__name__)


def speak_bot(text, lang='en'):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save(DEFAULT_FILE_SPEAk.format("speak", ran))
    return 0


@app.route('/')
def hello():
    return 'Hello World!!!'


@app.route('/speak', methods=['POST'])
def speak():
    if request.method == 'POST':
        val = request.get_json()['text']
        data = json.dumps({"sender": "Rasa", "message": val})
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain'}
        res = requests.post(
            'http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
        res = res.json()
        val = res[0]['text']
        speak_bot(val)
        return val
