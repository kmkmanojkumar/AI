from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time
import random
import pyttsx3
import speech_recognition as sr
# Login Credentials
#username = input('Enter your Username ')
username="rajeswaranpkt@gmail.com"
password="2003Raj$"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("to whom you want to send message")

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
'''while 1:
        query=listen()
        if len(query)!=0 or "stop" in query:
            break'''
dict={'gautam':"gowtham_badboy001",
      'manoj':"manoj_vishwa_04",
      'kamlesh':"i_kamalesh_15",
      'kamalesh':"i_kamalesh_15"}
url=url = 'https://instagram.com/' + dict[listen()]
#password = input('Enter your Password ')
#url = 'https://instagram.com/' + input('Enter username of user whome you want to send message')
def path():
        global chrome
     
        # starts a new chrome session
        chrome = webdriver.Chrome(ChromeDriverManager().install()) # Add path if required else empty .chrome()
        chrome.maximize_window()
def url_name(url):
  chrome.get(url)
   
  # adjust sleep if you want
  time.sleep(4)
def login(username, your_password):
    log_but = chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div[2]/div[1]/a/button")
    time.sleep(2)
    log_but.click()
    time.sleep(4)
     
    # finds the username box
    usern = chrome.find_element(By.NAME,"username")
     
    # sends the entered username
    usern.send_keys(username)
 
    # finds the password box
    passw = chrome.find_element(By.NAME,"password")
 
    # sends the entered password
    passw.send_keys(your_password)
     
    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)
     
    # Finding Not Now button
    try:
      notk = chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div") 
      notk.click()
      time.sleep(5)
    except:
      pass

def send_message():
   
    # Find message button
    message = chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div")
    message.click()
    time.sleep(10)
    try:
      chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
      time.sleep(1)
    except:
      pass
    
    '''l = ['hello', 'Hi', 'How are You', 'Hey', 'Bro whats up']
    for x in range(10):
        mbox = chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        mbox.send_keys(random.choice(l))
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)'''
    speak("what is the message sir")
    while 1:
        l=listen()
        if "done" in l or "stop" in l or "send" in l or "exit" in l:
            break
        mbox = chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        mbox.send_keys(l)
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)
    speak("message was sent sir")

path()
time.sleep(1)
url_name(url)
login(username, password)
send_message()
chrome.close()
