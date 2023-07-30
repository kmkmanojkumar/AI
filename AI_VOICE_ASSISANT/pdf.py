#pdf reader
import pyttsx3
import pdfplumber

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#with pdfplumber.open(r'C:/Users/manoj/Downloads/URBAN GREEN SPACES.pdf') as pdf:
speak("provide path of pdf here")
print("provide path of pdf here")
pdf=pdfplumber.open(r'C:/Users/manoj/Downloads/URBAN GREEN SPACES.pdf')
pages=(len(pdf.pages))
for i in range(pages):
    page = pdf.pages[i]
    text=(page.extract_text())
    print(text)
    sp=pyttsx3.init()
    sp.say(text)
    sp.runAndWait()

