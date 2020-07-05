import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import speech_recognition as sr
import datetime
import os
import random
import sys

# from googlesearch import search
# name
name = "Sohel"
userName = "  " + name

# relation
relation = "bro"

# Speed variables
slowSpeed = 180
mediumSpeed = 190
fastSpeed = 210

# Volume
speakVolume = 1  # Colume 0-1


# Language
searchLang = "en-in"

# gender id
genderId = 0


# default varirables/System paths
# pythonProjectFilePath = "F:\\Jarvis\\"
createPyFile = "F:\\Jarvis\\createPyProject.py"
createJsFile = "F:\\Jarvis\\createJsProject.py"
whatsappPath = "C:\\Users\\sohel\\AppData\\Local\WhatsApp\\WhatsApp.exe"
gameloopPath = "E:\program files\txgameassistant\appmarket\AppMarket.exe"
music_dir = "E:\\Music\\"

visualStudioCodePath = (
    "C:\\Users\\sohel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
)

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

incognito_chrome_path = (
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
)


passQuestions = ["my gorgeous friend", "in simplified", "my friend", relation.lower()]
passAnswers = [
    "internet",
    "web development",
    "you are amazing",
    relation.lower(),
]


def vaidatePostAction(number):
    speak("Password: ")
    passQuery = takeCommand().lower()
    if passAnswers[number] in passQuery:
        speak("Redirecting")
    else:
        speak("Incorrect Password")
        quit(0)


def validateAction(text):
    randomQues = random.randint(0, len(passQuestions) - 1)
    speak(text + ", " + passQuestions[randomQues])
    vaidatePostAction(randomQues)


# Pre requisite function code
def speakSpeed(speed):
    engine.setProperty("rate", speed)


# Open site in chrome
def open(site):
    webbrowser.get(chrome_path).open(site)


# Opens Chrome in Incognito Mode
def openPrivate(site):
    webbrowser.get(incognito_chrome_path).open(site)


# Searched Google
def googleSearch(searchQuery):
    return "https://google.com/search?q=" + searchQuery


# Open desired gmail inbox
def openInbox(number):
    if number == 1130:
        return "mail.google.com/mail/u/3/#inbox"

    elif number == 2212:
        return "mail.google.com/mail/u/0/#inbox"

    elif number == "contact":
        return "mail.google.com/mail/u/1/#inbox"

    elif number == "sohel editz":
        return "mail.google.com/mail/u/4/#inbox"


# pyttsx3 config
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[genderId].id)
speakSpeed(mediumSpeed)
engine.setProperty("volume", speakVolume)  # Volume 0-1

# os config
songs = os.listdir(music_dir)


# Wish user according to time
def wishUser():
    hour = int(datetime.datetime.now().hour)
    speakSpeed(slowSpeed)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + userName)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + userName)
    elif hour >= 18 and hour < 20:
        speak("Good Evening" + userName)
    else:
        speak("Good Night" + userName)

    speakSpeed(fastSpeed)
    speak("How may I help you" + relation)
    speakSpeed(mediumSpeed)


# Speack audio(argument) using pyttsx
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Takes caommand from mic using speech_recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language=searchLang)

        print(f"You said: {query}")

    except Exception as e:
        print(e)
        print("Say that agian...")
        return "None"

    return query


if __name__ == "__main__":
    wishUser()
    while True:
        query = takeCommand().lower()
        if "Hello Jarvis" in query:
            speak(f"Hello {userName}, tell me something!")

        elif "Jarvis tell me about you" in query:
            speak(
                f"Hello {userName}, I am Jarvis your personal assistant. I was build by Sohel Shekh. He coded me in python. I am here to simplify your work! Helping you is my work!"
            )

        elif "" in query:
            engine.setProperty("voice", voices[genderId].id)
            if "wikipedia" in query or "wiki" in query:
                speak("Searching Wiki...")
                query = query.replace("wikipedia", "")
                wikiResults = wikipedia.summary(query, sentences=2)
                print(wikiResults)
                speak("According to Wikipedia")
                speak(wikiResults)

            elif "open" in query:
                if "youtube" in query:
                    speak("Opening Youtube")
                    open("youtube.com")

                elif "google" in query:
                    speak("Opening Google")
                    open("google.com")

                elif "d2h.com" in query or "videocon d2h" in query:
                    speak("Opening Videocom D2H")
                    open("d2h.com")

                elif "insta" in query or "instagram" in query:
                    if "inbox" in query or "chat box" in query:
                        speak("Opening your Insta")
                        open("instagram.com/direct/inbox/")
                    else:
                        speak("Opening your Insta")
                        open("instagram.com")

                elif (
                    "vs code" in query
                    or "visual studio code" in query
                    or "code" in query
                ):
                    speak("Opening VS Code")
                    os.startfile(visualStudioCodePath)

                elif "whatsapp" in query:
                    validateAction("Opening Whatsapp")
                    os.startfile(whatsappPath)

                elif "pubg mobile" in query:
                    speak("Opening PUBG Mobile")
                    os.startfile(gameloopPath)

                elif "account" in query:
                    if "1130" in query:
                        validateAction("Opening sohelshekh1130 gmail inbox")
                        open(openInbox(1130))
                    elif "main" in query:
                        validateAction("Opening sohelshekh222005 gmail inbox")
                        open(openInbox(2212))
                    elif "contact" in query:
                        validateAction("Opening contactdotsohelshekh gmail inbox")
                        open(openInbox("contact"))
                    elif "sohel edits" in query:
                        validateAction("Opening sohel editz gmail inbox")
                        open(openInbox("sohel editz"))

                elif "incognito" in query or "private" in query:
                    if "youtube" in query:
                        speak("Opening YouTube in Incognito Mode")
                        openPrivate("youtube.com")
                    elif "insta" in query:
                        speak("Opening Insta in Incognito Mode")
                        openPrivate("instagram.com/direct/inbox")

            elif "search" in query:
                if "incognito" in query:
                    query = query.replace("search", "")
                    query = query.replace("in incognito", "")
                    speak(f"Searching {query} in incognito mode")
                    openPrivate(googleSearch(query))
                else:
                    query = query.replace("search", "")
                    speak(f"Searching {query}")
                    open(googleSearch(query))

            elif "start" in query:
                if "new" in query:
                    if "project" in query:
                        if "python" in query:
                            speak("Initializing Python Project")
                            os.system("python" + createPyFile)
                        else:
                            speak("Initializing JS Project")
                            os.system("python" + createJsFile)

            elif "play" in query:
                if "music" in query or "song" in query or "songs" in query:
                    if "random" in query:
                        randomSong = random.randint(0, len(songs))
                        speak("Playing " + songs[randomSong - 1])
                        os.startfile(os.path.join(music_dir, songs[randomSong - 1]))
                    else:
                        os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)
                print(strTime)

            elif "change your gender" in query:
                if genderId == 0:
                    speak("Changing to Zira")
                    genderId = 1
                else:
                    speak("Changing to David")
                    genderId = 0
            
            elif "stop" in query:
                if "jarvis" in query:
                    exit(0) 
