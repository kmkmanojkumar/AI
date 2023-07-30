import speech_recognition as sr
import wikipedia
import pyttsx3
import os
#pip install googletrans
#from googletrans import Translator         #pip install pyaudio
#from translate import Translator           #pip install translate
                                     #pip install speechrecognition

import pyttsx3 #pip install selenium==4.1.3(chrome based)
                #pip install pyttsx3(window based)

def speak(Text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',170)
    print()
    print(f"you:{Text}")
    print()
    engine.say(Text)
    engine.runAndWait()


def listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("LIstening.....")
        r.pause_threshold=1
        audio= r.listen(source,0,6)
    try:
        print("rec...")
        query=r.recognize_google(audio,language="en-IN")

    except:
        return ""
    query=str(query).lower()
    return query
#listen()

def Mic():
    query=listen()
    data=(query)
    return data
#Mic()

import openai
from dotenv import load_dotenv

openai.api_key="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"
load_dotenv()
completion=openai.Completion()

def replybrain(question,chat_log=None):
    filelog=open("C:/Users/manoj/Downloads/chat_log.txt","r")
    chat_log_template=filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log=chat_log_template

    prompt=f'{chat_log}You: {question}\nJarvis:'
    response=completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
        )
    answer=response.choices[0].text.strip()
    #chat_log_template_update=""
    chat_log_template = chat_log_template + f"\n you :{question} \n jarvis:{answer}"
    filelog=open("C:/Users/manoj/Downloads/chat_log.txt","w")
    filelog.write(chat_log_template)
    filelog.close()
    return answer
#pyttsx3.speak(replybrain("about ml"))'''
speak("chat with openai bot")
speak("no or stop or exit for stop the process")
while 1:
    t=Mic()
    t=str(t)
    print(t)
    if 'no' in t or 'stop' in t or 'exit' in t:
        break
    speak(replybrain(t))
print("Bye")
