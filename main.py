import speech_recognition as sr
import datetime
# from pygame import mixer
# from datetime import datetime
# from time import time
from googletrans import Translator
import random
import ctypes
import pyttsx3
import wikipedia
import sounddevice
from scipy.io.wavfile import write
import os
import webbrowser
import smtplib
import base64
import requests
import json
from selenium import webdriver
from gtts import gTTS
import playsound
import wolframalpha
import string

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def getdate():
    import datetime
    return datetime.datetime.now()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir Please tell me how may I help you!")


def recorder0():
    fs = 44100
    speak("How long you want to record?")
    print("How long you want to record?")
    query0 = takeCommand().lower()
    if 'second' in query0:
        speak("Type in the number")
        second = int(input("Enter the no. of second = "))
    elif 'minute' in query0:
        speak("Type in the number")
        second = int(input("Enter the no. of minute = "))
        minute = int(input())
        second = 60*minute
    elif 'hours' in query0:
        speak("Type in the number")
        second = int(input("Enter the no. of hours = "))
        hours = int(input())
        second = 60*60*hours
    else:
        print("Invalid entry")
        speak("Invalid entry, Please try again")
        return
    print("recording....")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    speak("Say, the name of audio file")
    print("Say, the name of audio file")
    output = takeCommand().lower()
    write(output+".wav", fs, record_voice)
    return


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Youremailaddress@email.com', 'YourPassword')
    server.sendmail('Youremailaddress@email.com', to, content)
    server.close()


def read_news(input):
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a68d16adea2e4fdb9d1c49982c72cbe7"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    print(news_dict["articles"])
    for article in arts:
        while True:
            query_1 = takeCommand().lower()
            if 'stop' in query_1 or 'exit' in query_1:
                speak("OK, Sir")
                return
            else:
                print(article['title'])
                speak("Moving on the next news...")
                speak(article['title'])
                break
    speak("Thanks for listening")
    print("Thanks for listening")
    return


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'jarvis shutdown' in query or 'shutdown jarvis' in query or 'jarvis sleep' in query or 'sleep jarvis' in query:
            speak("Ok sir, as you command")
            exit()

        elif 'hello' in query or 'hi' in query:
            speak("Hello! What I am doing for you!")

        elif 'your name' in query:
            speak("Sir, My name is Jarvis.")

        elif 'your creater' in query or 'your developer' in query:
            speak("Sir, My creater name is Mr. Gurbaksh Bradh.")

        elif 'whats up' in query:
            speak("I am fine, and you!")

        elif 'jarvis' in query:
            speak("As your command Sir...")

        elif 'open whatsapp in chrome' in query or "open whatsapp" in query:
            speak("Opening Whatsapp")
            chromedriver = os.path.join(os.getcwd(), 'Chrome/chromedriver.exe')
            driver = webdriver.Chrome(chromedriver)
            driver.get("https://web.whatsapp.com/")

        elif 'email' in query:
            try:
                dicMail = {
                    'me': 'Youremailaddress@email.com',
                    'friend': 'Yourfriendemailaddress@email.com'
                }
                speak("What should I say?")
                content = takeCommand()
                speak('To')
                select = takeCommand().lower()
                to = dicMail[select]
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! Sir, I am not able to send this email.Please Try again...")

        elif 'news' in query:
            read_news(query)

        elif 'play music' in query or 'music play' in query or 'song play' in query or 'music song' in query:
            speak("Playing music")
            music_dir = os.path.join(os.getcwd(), 'Music')
            songs = os.listdir(music_dir)
            randomfile = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomfile))

        elif 'record' in query or 'recorde' in query or 'recorder' in query:
            recorder0()

        elif "list directory c" in query:
            speak("Ok, sir")
            list_dir01 = os.listdir("C:\\")
            print(list_dir01)

        elif "list directory d" in query:
            speak("Ok, sir")
            list_dir01 = os.listdir("D:\\")
            print(list_dir01)

        elif "open cd" in query:
            speak("Opening CD ROM")
            ctypes.windll.WINMM.mciSendStringW(
                u"set cdaudio door open", None, 0, None)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'show task list' in query:
            speak("Showing Task List")
            os.system('TASKLIST')

        elif 'open notepad' in query:
            speak("Opening notepad")
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("Closing notepad")
            os.system('TASKKILL /F /IM notepad.exe')

        elif "open chrome" in query:
            speak("Opening Google Chrome")
            os.startfile(
                'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

        elif "close chrome" in query:
            speak("Closing Google Chrome")
            os.system('TASKKILL /F /IM chrome.exe')

        elif "open firefox" in query or "open mozilla" in query:
            speak("Opening Mozilla Firefox")
            os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

        elif "close firefox" in query or "force to close mozilla" in query:
            speak("Closing Mozilla Firefox")
            os.system('TASKKILL /F /IM firefox.exe')

        elif "open word" in query:
            speak("Opening Microsoft Word")
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

        elif "close word" in query:
            speak("Closing Microsoft Word")
            os.system('TASKKILL /F /IM WINWORD.EXE')

        elif "open excel" in query:
            speak("Opening Microsoft Excel")
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

        elif "close excel" in query:
            speak("Closing Microsoft Excel")
            os.system('TASKKILL /F /IM EXCEL.EXE')

        elif "open powerpoint" in query:
            speak("Opening Microsoft Powerpoint")
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')

        elif "close powerpoint" in query:
            speak("Closing Microsoft Powerpoint")
            os.system('TASKKILL /F /IM POWERPNT.EXE')

        elif "open onenote" in query:
            speak("Opening Microsoft OneNote")
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')

        elif "close onenote" in query:
            speak("Closing Microsoft OneNote")
            os.system('TASKKILL /F /IM ONENOTE.EXE')

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("http://www.youtube.com/")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")

        elif "open snipping" in query or "crop" in query:
            speak("Ok, Sir")
            os.startfile("C:\\Windows\\System32\\SnippingTool.exe")

        elif "open wikipedia" in query:
            speak("Opening wikipedia")
            webbrowser.open("https://en.wikipedia.org/")

        elif "open youtube in chrome" in query:
            speak("Opening Youtube")
            chromedriver = os.path.join(os.getcwd(), 'Chrome/chromedriver.exe')
            driver = webdriver.Chrome(chromedriver)
            driver.get("http://www.youtube.com/")

        elif "open wikipedia in chrome" in query:
            speak("Opening Wikipedia...")
            chromedriver = os.path.join(os.getcwd(), 'Chrome/chromedriver.exe')
            driver = webdriver.Chrome(chromedriver)
            driver.get("https://en.wikipedia.org/")

        elif 'open google in chrome' in query:
            speak("Opening Google...")
            chromedriver = os.path.join(os.getcwd(), 'Chrome/chromedriver.exe')
            driver = webdriver.Chrome(chromedriver)
            driver.get("https://www.google.com/")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            speak("How many sentence I read?")
            print("How many sentence I read?")
            speak("Type for integer")
            n = takeCommand()
            results = wikipedia.summary(query, sentences=n)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'calculate' in query or 'about' in query:
            query = query.replace("about", "")
            app_id = "K9P82T-66V594VUJ8"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'translate' in query:
            query = query.replace("translate", "")
            text = query
            destiation_language = {
                'English': 'en',
                'Hindi': 'hi'
            }
            translator = Translator()
            for key, value in destiation_language.items():
                ans = translator.translate(text, dest=value).text
                print(ans)
                speak(ans)

        elif 'shutdown laptop' in query or 'shutdown pc' in query or 'shutdown computer' in query:
            speak("Ok, Sir")
            os.system("shutdown /s /t 1")
            break

        elif 'restart laptop' in query or 'restart pc' in query or 'restart computer' in query:
            speak("Ok, Sir")
            os.system("shutdown /r /t 1")
            break

        elif 'computer sleep' in query or 'laptop sleep' in query or 'pc sleep' in query or 'sleep laptop' in query or 'sleep pc' in query or 'sleep computer' in query:
            speak("Ok, Sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            break
