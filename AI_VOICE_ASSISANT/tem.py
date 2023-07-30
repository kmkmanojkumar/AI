import requests
from bs4 import BeautifulSoup   #ctrl+w to close single tab in chrome
import pyttsx3                #ctrl+shift+t to reload closed tab
import pyautogui
import speech_recognition as sr   #pip install googletrans
import googletrans      #pip install googletrans==3.1.0a0
from googletrans import Translator         #pip install pyaudio #pip install translate
import os
import time
import pywhatkit                         #pip install speechrecognition
import datetime
from datetime import timedelta
from datetime import datetime
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
#listen()

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.setProperty("rate",170)
    print()
    print(f"you:{Text}")
    print()
    engine.say(Text)
    engine.runAndWait()
def gtts(text,lan):
    # Import the required module for text 
    # to speech conversion
    from gtts import gTTS
    import pyautogui as p
    # This module is imported so that we can 
    # play the converted audio
    import os
    from playsound import playsound  
    # The text that you want to convert to audio
    mytext =text
      
    # Language in which you want to convert
    language = 'en'
      
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
      
    # Saving the converted audio in a mp3 file named
    # welcome
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    myobj.save("C:\\Users\\manoj\\OneDrive\\Desktop\\AI_VOICE_ASSISANT\\tran_voice\\"+filename)
      
    # Playing the converted file
    playsound("C:\\Users\\manoj\\OneDrive\\Desktop\\AI_VOICE_ASSISANT\\tran_voice\\"+filename)

def listen1(fro):
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("LIstening.....")
        r.pause_threshold=1
        audio= r.listen(source,0,8)
    try:
        print("rec...")
        query=r.recognize_google(audio,language=fro)
        
    except:
        return ""
    query=str(query).lower()
    return query
#listen()
def Translate(Text,fro):
    from main import tk1
    languages=googletrans.LANGUAGES
    print("to which language:")
    speak("to which language:")
    to=listen()
    print(to)
    print("selected language is ",list(languages.keys())[list(languages.values()).index(to)])
    to=list(languages.keys())[list(languages.values()).index(to)]
    translator = Translator()
    result = translator.translate(Text, src=fro, dest=to)
    print(result.src)
    print(result.dest)
    data=result.text
    print(f"You:{data}")
    gtts(data,fro)
    tk1(data)
    return data
def translator():
    print(googletrans.LANGUAGES)
    languages=googletrans.LANGUAGES
    print("from which language:")
    speak("from which language:")
    fro=listen()
    print(fro)
    print("selected language is ",list(languages.keys())[list(languages.values()).index(fro)])
    fro=list(languages.keys())[list(languages.values()).index(fro)]
    speak("what do you need to translate sir")
    text=listen1(fro)
    print(text)
    Translate(text,fro)
#translator()
    
def Mic():
    query=listen()
    data=(query)
    return data
#Mic()
def temperature():
    search="temperature in chennai"
    url=f"https://www.google.com/search?q={search}"
    u=requests.get(url)
    data=BeautifulSoup(u.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    #weather=data.find("div",class_="VQF4g").text
    print(temp)
    #print(data)
#temperature()

import datetime as dt
def time():
    actualTime = dt.datetime.now()
    currentTime = actualTime.strftime("%H : %M : %S")
    currentDate = actualTime.strftime("%d / %m / %Y")
    print(currentTime+"__ "+currentDate)
#time()

def remember(query):
     msg=query.replace("remember that","")
     print("you told to remember that "+msg)
     rem=open("rem.txt","a")#a to append #w to write replace txt newly #r to read
     
     rem.write(f"{msg}\n")
     #rem.write(",")
     rem.close()
remember("remember that today")
def what():
    rem=open("rem.txt","r")
    #b=rem.read()
    #a=list(b.split(","))
    #print(a)
    '''if len(a)>1:
        for i in range(len(a)):
            if i==len(a)-1:
                break
            if i!=0:
                speak("and also")
            speak("you told me to remember that"+a[i])'''
    speak("you told me to remember that"+rem.read())
    speak("did you want to delete this:")
    i=input("y/n")
    if i=="y":
        deletetime = open("rem.txt","r+")
        deletetime.truncate(0)
        deletetime.close()
    else:
        pass
what()

from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def control():
    query=input()
    print(query)
    if "pause" in query:
        pyautogui.press("k")
        speak("video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("video played")
    elif "mute" in query:
        pyautogui.press("m")
        speak("video muted")
    elif "volume up" in query:
        speak("Turning volume up,sir")
        volumeup()
    elif "volume down" in query:
        speak("Turning volume down, sir")
        volumedown()
    elif "scroll" in query:
        speak("scrolling sir")
        pyautogui.scroll(10)
        
#control()
def scroll():
    for s in range(20):
        pyautogui.scroll(1)
        time.sleep(0.5)
#scroll()

def open(text):
    from AppOpener import open, close
    import pyautogui as p
    import webbrowser as w
    open("help")
    print("TRY 'OPEN <any_key>'")
    open("update")
    app_name = text.replace("open ","").replace("launch","").replace(" ","")
    speak(f"launching {app_name}")
    if "chrome" in text or "google" in app_name :
        w.open_new_tab("https://www.google.com/")
    elif "youtube" in app_name:
        w.open_new_tab("https://www.youtube.com/")
    elif ".com" in app_name or ".co.in" in app_name or ".org" in app_name:
        w.open(f"https://www.{app_name}")
    else:
        open(app_name, match_closest=True)
#open("launch chrome.com")
def close(text):
    from AppOpener import open, close
    import pyautogui as p
    import webbrowser as w
    open("help")
    print("TRY 'close <any_key>'")
    open("update")
    app_name = text.replace("close ","").strip()
    speak(f"closing {app_name}")
    close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
    p.hotkey('alt','F4')
        



    
def shut():
    query=input("enter:")
    if "shutdown" in query:
        speak("Are You sure you want to shutdown")
        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
        if shutdown == "yes":
            os.system("shutdown /s /f /t 20")
        elif shutdown == "no":
            return
    if "restart" in query:
        speak("Are You sure you want to restart")
        shutdown = input("Do you wish to restart your computer? (yes/no)")
        if shutdown == "yes":
            os.system("shutdown /r /t 20")
            pyautogui.press("enter")
        elif shutdown == "no":
            return
#shut()
def abort():
    query=input("enter:")
    if "abort shutdown" in query:
        speak("aborting the shutdown")
        os.system("shutdown /a ")
    elif "abort restart" in query:
        speak("aborting the restart")
        os.system("shutdown /a ")
        
#abort() 

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    #r()
    os.startfile("alarm.py")

def alarming():
        print("input time example:- 10 and 10 and 10")
        speak("Set the time")
        a = input("Please tell the time :- ")
        alarm(a)
        speak("Done,sir")
#alarming()


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 1)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg_instantly("+916382818186",message)
    elif a==2:
        pass

#sendMessage()

def schedule():
    tasks = [] #Empty list 
    speak("Do you want to clear old tasks (Plz speak YES or NO)")
    query =input()
    if "yes" in query:
        file = open("tasks.txt","w")
        file.write(f"")
        file.close()
        no_tasks = int(input("Enter the no. of tasks :- "))
        i = 0
        for i in range(1,no_tasks+1):
            tasks.append(input("Enter the task :- "))
            file = open("tasks.txt","a")
            file.write(f"{i}. {tasks[i-1]}\n")
            file.close()
    elif "no" in query:
        i = 0
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(1,no_tasks+1):
            tasks.append(input("Enter the task :- "))
            file = open("tasks.txt","a")
            file.write(f"{i}. {tasks[i-1]}\n")
            file.close()
#schedule()

from notifypy import Notify  #pip install notify-py

no = Notify()

from plyer import notification #pip install plyer
from pygame import mixer
def show():
    file = open("tasks.txt","r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load("wake.wav")
    mixer.music.play()
    notification.notify(
        title = "My schedule :-",
        message = content,
        timeout = 15
        )
#show()


import speedtest #pip install speedtest-cli
def internet():
     wifi  = speedtest.Speedtest()
     upload_net = wifi.upload()/1048576 #Megabyte = 1024*1024 Bytes
     download_net = wifi.download()/1048576
     upload_net=f"{upload_net:.2f}"
     download_net="%.2f"%download_net
     print("Wifi Upload Speed is", upload_net)
     print("Wifi download speed is ",download_net)
     speak(f"Wifi download speed is {download_net} mb per second")
     speak(f"Wifi Upload speed is {upload_net} mb per second")
#internet()

def ipl():
        from plyer import notification  #pip install plyer
        import requests #pip install requests
        from bs4 import BeautifulSoup #pip install bs4
        url = "https://www.cricbuzz.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")
        team1 = soup.find(class_ = "cb-col-50 cb-ovr-flo cb-hmscg-tm-name").findNext("span",class_="text-normal").get_text()
        team2 = soup.find("div",class_="cb-hmscg-tm-bwl-scr cb-font-14").findNext("span",class_="text-normal").get_text()
        team1_score = soup.find("div",class_ = "cb-col-50 cb-ovr-flo").get_text()
        team2_score = soup.find("div",class_="cb-hmscg-tm-bwl-scr cb-font-14").findNext(class_ = "cb-col-50 cb-ovr-flo").get_text()

        speak(f"{team1} : {team1_score}")
        speak(f"{team2} : {team2_score}")
        notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
#ipl()

def screenshot():
    im = pyautogui.screenshot()
    im.save("ss.jpg")
#screenshot()

def camera():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(10)
    speak("SMILE")
    pyautogui.press("enter")
    pyautogui.sleep(4)
    pyautogui.hotkey("alt","F4")
#camera()





def focus():
        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
        if (a==1):
            speak("Entering the focus mode....")
            os.startfile("FocusMode.py")
            exit()

        else:
            pass
#focus()


#pip install matplotlib
import matplotlib.pyplot as pt

def showfocus():
    os.startfile("showfocus.py")
#showfocus()
def news():
    os.startfile("news.py")
#news()
def calculator(query):
    if "calculate" in query:
        from Cal import Wolfram
        from Cal import calc
        query = query.replace("calculate","")
        query = query.replace("jarvis","")
        calc(query)
#calculator("calculate 2 power 2")
def game():
    os.startfile("game.py")
#game()
