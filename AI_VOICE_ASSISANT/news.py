import requests
import json
import pyttsx3
import pyautogui as p
import speech_recognition as sr 
import webbrowser
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
def listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("LIstening.....")
        r.pause_threshold=1
        audio= r.listen(source,0,8)
    try:
        print("rec...")
        query=r.recognize_google(audio,language="en-IN")

    except:
        return ""
    query=str(query).lower()
    print(query)
    return query

def Mic():
    query=listen()
    data=(query)
    return data

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b182dab296c344bc8e264ae8bb0bdedb",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b182dab296c344bc8e264ae8bb0bdedb",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=b182dab296c344bc8e264ae8bb0bdedb",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=b182dab296c344bc8e264ae8bb0bdedb",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b182dab296c344bc8e264ae8bb0bdedb",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b182dab296c344bc8e264ae8bb0bdedb"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field =listen()
    print(field)
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        speak("do you want to know more about it")
        more=listen()
        if "yes" in more:
            webbrowser.open_new_tab(news_url)
            speak("tell close tab to close it")
            while 1:
                close=Mic()
                if "close" in close:
                    p.hotkey("ctrl","w")
                    break
                elif "next" in close:
                    break
                else:
                    pass
        else:
            speak("do you want to continue")
            a = Mic()
            if "yes" in a:
                pass
            else:
                break
            
    speak("thats all")
latestnews()
