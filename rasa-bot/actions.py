import os
import pyttsx3
import random
import string
import speech_recognition as sr
from gtts import gTTS

DEFAULT_FILE_SPEAk = "./rasa-bot/audio/speak/{}-{}.wav"
# Initialize the recognizer
# r = sr.Recognizer()


# def SpeakText(command):

#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()


# Loop infinitely for user to
# speak

# while(1):

#     # Exception handling to handle
#     # exceptions at the runtime
#     try:

#         # use the microphone as source for input.
#         with sr.Microphone() as source2:

#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)

#             # listens for the user's input
#             audio2 = r.listen(source2)

#             # Using ggogle to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()

#             print("Did you say "+MyText)
#             SpeakText(MyText)

#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     except sr.UnknownValueError:
#         print("unknown error occured")


def speak(text, lang='en'):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save(DEFAULT_FILE_SPEAk.format("speak", ran))
    return 0
