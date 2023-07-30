from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time
import random
import pyautogui as p
import pyttsx3                #ctrl+shift+t to reload closed tab
import speech_recognition as sr  
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

def speak(Text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    print()
    print(f"you:{Text}")
    print()
    engine.say(Text)
    engine.runAndWait()

    
# Login Credentials
#username = input('Enter your Username ')
username="717821i119@kce.ac.in"
password="!Gowthaman@#119!"
url=url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox' 
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
  time.sleep(5)
def login(username, your_password):
    log_but = chrome.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
  
    log_but.click()
    log_but.send_keys(username)

    log_but.send_keys(Keys.RETURN)
    time.sleep(5.5)
    log_but1 = chrome.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    log_but1.send_keys(your_password)

    log_but1.send_keys(Keys.RETURN)
    time.sleep(20)
  
     
def send_message():
   
    # Find message button
    message = chrome.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div")
    message.click()
    time.sleep(5)
    speak("TO WHO DO YOU WANT TO SEND EMAIL,SIR")
    while 1:
        a=listen()
        print(a)
        if len(a)!=0:
            if "gautam" in a:
                a="gowthaman"
                break
            else:
                break
        
    p.typewrite(a)
    p.press("enter")
    time.sleep(4)
    chrome.find_element(By.XPATH,"/html/body/div[16]/div[2]/div[3]/button[2]").click()
    time.sleep(5)
    subject_input = chrome.find_element(By.NAME,'subjectbox')
    speak("WHAT IS THE SUBJECT SIR")
    c=listen()
    print(c)
    subject_input.send_keys(c)
    time.sleep(5)
    body_input = chrome.find_element(By.XPATH,'//div[@role="textbox"]')
    speak("WHAT IS THE MESSAGE SIR")
    while 1:
        b=listen()
        print(b)
        if len(b)!=0:
            break
    body_input.send_keys(b)
    time.sleep(5)
    send_button = chrome.find_element(By.XPATH,'//div[text()="Send"]')
    send_button.click()
    time.sleep(10)
    speak("MAIL WAS SENT SUCCESSFULLY SIR")

path()
time.sleep(1)
url_name(url)
login(username, password)
send_message()
chrome.close()
