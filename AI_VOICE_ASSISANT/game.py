import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    speak("1-rock  2-paper  3-scissors")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = listen()
        if "first" in query or "1" in query or "rock" in query:
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif ("p" in query or "2" in query or "paper" in query ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif ("3" in query or "s" in query  or "scissors" in query or "scissor" in query or "f" in query):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
    speak(f"FINAL SCORE :- you :- {Me_score} : computer :- {Com_score}")
    if Me_score > Com_score:
        speak("you won the match,sir")
    elif Me_score < Com_score:
        speak("you loss the match,sir")
    else:
        speak("match was draw,sir")
    
game_play()
            

