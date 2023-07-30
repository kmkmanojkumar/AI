import datetime
import webbrowser
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import pywhatkit
import keyboard as k
import time
from datetime import datetime



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()

for i in range(3):
    speak("Enter Password to open Jarvis :- ")
    print("Enter Password to open Jarvis :- ")
    a=takeCommand()
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        print("you entered the wrong password")
        speak("you entered the wrong password")
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        print(f"You Said: {query}\n")
        if "wake up" in query or "makeup" in query or "tommy" in query or "up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
                #################### JARVIS: THe Trilogy 2.0 #####################

                elif "change password" in query or "change the password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        i = 0
                        speak("Enter the no. of tasks :- ")
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            speak("Enter the task :- ")
                            tasks.append(takeCommand())
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        speak("Enter the no. of tasks :- ")
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            speak("Enter the task :- ")
                            tasks.append(takeCommand())
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("focusmode.py")
                        #exit()
                        


                    
                    else:
                        pass

                elif "show my focus" in query:
                    os.startfile("showfocus.py")

                elif "translate" in query:
                    from tem import translator
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translator()

                elif "open facebook" in query :
                    os.startfile("facebook.py")
                
                elif "open instagram" in query or "send message in instagram" in query:
                    os.startfile("instagram.py")

                elif "open email" in query or "send email" in query:
                    os.startfile("mail.py")

                elif "virtual mouse" in query or "mouse" in query:
                    os.startfile("virtualmouse.py")

                elif "pdf reader" in query:
                    os.startfile("pdf.py")
                
                elif "chat with bot" in query or "chat" in query:
                    os.startfile("chatbot.py")
                
                elif "joke" in query or "jokes" in query:
                    import pyjokes as p
                    a=p.get_joke(language="en",category="neutral")
                    print(a)
                    speak(a)

                elif "find location" in query or "location of number" in query:
                    os.startfile("location_number.py")

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    from AppOpener import open, close
                    import pyautogui as p
                    import webbrowser as w
                    open("help")
                    print("TRY 'OPEN <any_key>'")
                    open("update")
                    app_name = query.replace("open ","").replace("launch","").replace(" ","")
                    speak(f"launching {app_name}")
                    if "chrome" in app_name or "google" in app_name :
                        w.open_new_tab("https://www.google.com/")
                    elif "youtube" in app_name:
                        w.open_new_tab("https://www.youtube.com/")
                    elif ".com" in app_name or ".co.in" in app_name or ".org" in app_name:
                        w.open(f"https://www.{app_name}")
                    elif "camera" in app_name:
                        pyautogui.press("super")
                        pyautogui.typewrite(app_name)
                        pyautogui.sleep(2)
                        pyautogui.press("enter") 
                    else:
                        open(app_name, match_closest=True)
                elif "close" in query:
                    if "close the tab" in query:
                        speak("closing the tab")
                        pyautogui.hotkey("ctrl","w")
                    elif "close the chrome" in query or "close chrome" in query:
                        close("chrome", match_closest=True, output=False)
                    elif "close camera" in query:
                        p.hotkey('alt','F4')
                    else:
                        query = query.replace("close","")
                        query = query.replace("jarvis","")
                        from AppOpener import open, close
                        import pyautogui as p
                        import webbrowser as w
                        open("help")
                        print("TRY 'close <any_key>'")
                        open("update")
                        app_name =query.replace("close ","").strip()
                        speak(f"closing {app_name}")
                        close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
                        p.hotkey('alt','F4')
                        
                     
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576 #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    upload_net=f"{upload_net:.2f}"
                    download_net="%.2f"%download_net
                    print("Wifi Upload Speed is"+ upload_net+"mb")
                    print("Wifi download speed is "+download_net+"mb")
                    speak(f"Wifi download speed is {download_net} mb per second")
                    speak(f"Wifi Upload speed is {upload_net} mb per second")
                    

                elif "ipl score" in query:
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
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                                    title = "IPL SCORE :- ",
                                    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                    timeout = 15
                                )
                            
                elif "play a game" in query:
                    os.startfile("game.py")

                elif "screenshot" in query:
                     speak("taking screenshot")
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     date_string = datetime.now().strftime("%d%m%Y%H%M%S")
                     filename = "ss"+date_string+".jpg"
                     im.save("C:\\Users\\manoj\\OneDrive\\Desktop\\AI_VOICE_ASSISANT\\screenshot\\"+filename)

                elif "click photo" in query or "snap" in query:
                   speak("taking photo")
                   os.startfile("camera.py")

                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=g-NW7ldObWk")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=Zllqm2zHmpA&list=RDg-NW7ldObWk&start_radio=1")
                    if b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=DnyA_qEbTpw")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                


                elif "volume up" in query:
                    from tem import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from tem import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

               
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    os.startfile("news.py")

                elif "calculate" in query:
                    from Cal import Wolfram
                    from Cal import calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    calc(query)

                elif "whatsapp" in query:
                    speak("Who do you wan to message")
                    print('''Person 1 - gowthaman
                    Person 2 - kamalesh
                    person 3 - manoj kumar''')
                    a=takeCommand()
                    if "1" in a or "gautam" in a or "gowthaman" in a or "gowtham" in a:
                        speak("Whats the message")
                        message = takeCommand()
                        import keyboard as k
                        pywhatkit.sendwhatmsg_instantly("+916382818186", message)
                        pyautogui.click(1050, 950)
                        time.sleep(2)
                        pyautogui.hotkey("alt","F4")
                        k.press_and_release('enter')
                    elif "2" in a or "kamalesh" in a or "kamlesh" in a:
                        speak("Whats the message")
                        message =takeCommand()
                        pywhatkit.sendwhatmsg_instantly("+916383880615",message)
                        pyautogui.click(1050, 950)
                        time.sleep(2)
                        pyautogui.hotkey("alt","F4")
                    elif "3" in a or "manoj kumar" in a or "manoj" in a:
                        speak("Whats the message")
                        message = takeCommand()
                        pywhatkit.sendwhatmsg_instantly("+919566970257",message)
                        pyautogui.click(1050, 950)
                        time.sleep(2)
                        pyautogui.hotkey("alt","F4")

                

                elif "temperature" in query:
                    speak("tell place to see temperature")
                    search = takeCommand()
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(f"current{search} is {temp}")
                elif "weather" in query:
                    search = query
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                    print("Done,sir")
                           
                elif "the time" in query or "time" in query:
                    import datetime as dt
                    actualTime = dt.datetime.now()
                    currentTime = actualTime.strftime("%H : %M : %S")
                    currentDate = actualTime.strftime("%d / %m / %Y")
                    print(currentTime+"__ "+currentDate)   
                    speak(f"Sir, the time is {currentTime} and date is {currentDate}")
                elif "sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())
                    speak("did you want to delete this:")
                    i=takeCommand()
                    if i=="yes":
                        deletetime = open("Remember.txt","r+")
                        deletetime.truncate(0)
                        deletetime.close()
                    else:
                        pass
    
                elif "abort restart" in query or "cancel restart" in query or "cancel" in query:
                    speak("aborting the restart")
                    os.system("shutdown /a ")

                elif "abort shutdown" in query or "cancel shutdown" in query or "cancel" in query:
                    speak("aborting the shutdown")
                    os.system("shutdown /a ")

                elif "shutdown" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = takeCommand()
                    if shutdown == "yes" or "yes" in shutdown or "y" in shutdown:
                        os.system("shutdown /s /t 30")


                    elif shutdown == "no":
                        pass
                elif "restart" in query:
                    speak("Are You sure you want to restart")
                    shutdown = takeCommand()
                    if shutdown == "yes" or "yes" in shutdown or "y" in shutdown:
                        os.system("shutdown /r /t 30")
                        pyautogui.press("enter")
                    elif shutdown == "no":
                        pass
                
                    
        elif "sleep" in query:
            speak("Thank you sir..Have a good day")
            break
        

                




                


 
