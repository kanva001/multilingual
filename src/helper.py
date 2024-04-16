import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

print("perfect !")

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY


# code fot voice assitnat

def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening..")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    except sr.RequestError as e:
        print("Could not request result from Speech Recognition service: {0}".format(e))
    

def text_to_speech(text):
    tts=gTTS(text=text, lang='en')
    
    # Save the speech from the given test in the .mp3 format
    tts.save("speech.mp3")
    

def llm_model_object(user_text):
    model="model/gemini-pro"
    
    model = genai.GenerativeModel(model)
    response = model.generate_content(user_text)
    result = response.text
    
    return result

