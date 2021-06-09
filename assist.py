import psutil
import platform
import pyttsx3
import datetime
import calendar
from tkinter import *
import time
import wikipedia
import webbrowser
import os
import pyowm
import speech_recognition as sr
import smtplib


engine = pyttsx3.init('sapi5')
voiceRate = 40
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        speak("Good afternoon sir")
    else:
        speak("good Evening sir")
    speak("I am jarvis sir") 
    speak(" your assistant")
    speak("how i can help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    em = open("em.txt", "r")
    for line in em:
        a = line.rstrip()
    ep = open("pass.txt", "r")
    for line in ep:
        b = line.rstrip()
    
    server.login(a,b)
    server.sendmail(em, to, content)
    server.close()

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listenig....")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
         print("Recognizing....")
         query = r.recognize_google(audio,  language = 'en-in')
         print(f"You said: {query}\n")

     except:
        print(" Say that again please....")
        
        return "none"
     return query
     speak("next command please")



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open google" in query:
            speak("opening google chrome ")
            os.startfile("chrome.exe")

        elif "close google" in query:
            speak("closing google chrome")
            os.system("TASKKILL /F /IM chrome.exe" )
 
       
        elif " on google" in query:
            query = query.replace("on google"," ")
            print(query)
            query = query.replace("search"," ")
            url='https://www.google.com/search?q='
            search_url=url+query
            webbrowser.open(search_url)
            print(query)
            speak("searchig on google..")

        elif "open youtube" in query:
            speak("opening youtube..")
            webbrowser.open("youtube.com")

        
            
        elif "on youtube" in query:
            query = query.replace("on youtube"," ")
            url = 'https://www.youtube.com/results?search_query='
            search_url= url+query
            webbrowser.open(search_url)
            print(query)
            speak("searching on youtube..")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:")
            speak(f" sir the time is {strTime}")

        elif "visual studio" in query:
            speak("opening Visual studio...")
            codePath = r'C:\\Users\\aditya\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif "close visual studio" in query:
            speak("closing visual studio..")
            os.system("TASKKILL /F /IM code.exe" )



        elif "open python" in query:
            codePath = r'C:\\Users\\aditya\\AppData\\Local\\Programs\\Python\\Python37-32\\pythonw.exe '
            os.startfile(codePath)

        elif "W3 school" in query:
            speak("opening w3 schools.com")
            webbrowser.open("w3school.com")

        elif "on w3school" in query:
            url= 'https://www.w3schools.com/'
            search_url=url+query
            webbrowser.open(search_url)
        
        elif "open tutorials point" in query:
            webbrowser.open("tutorialspoint.com")
        
        elif "on tutuorials point" in query:
            query = query.replace("on tutorials point", " ")
            url = "https://www.tutorialspoint.com/"
            search_url = url+query
            webbrowser.open(search_url)

        elif " the date" in query:
            localtime = time.asctime( time.localtime(time.time()) )
        
            speak(f" sir today is {localtime}")
            
        elif " open my computer" in query:
            os.system('explorer')
            speak("opening my computer")
            
            
        elif "control panel" in query:
            speak("opening control panel")
            os.system("cmd /c control")

        elif "close control panel" in query:
            speak("closing control panel")
            os.system("TASKKILL /F /IM control.exe" )


        elif "open computer" in query:
            speak("opening my computer")
            os.system("cmd /c explorer")

        elif "close computer" in query:
            speak("closing my computer")
            os.system("TASKKILL /F /IM explorer")


        elif "open notepad" in query:
            speak("opening my computer")
            os.startfile("notepad.exe")


        elif "close notepad" in query:
            speak("closing notepad")
            os.system("TASKKILL /F /IM notepad.exe" )

        elif "email to" in query:
            #re = {"me":"kadam96ganesh@gmail.com", "aniket":"aniket.deshmukh102@gmail.com", "ankita":"ankitakadam209@gmail.com"}
            query = query.replace('email to', '')
            #em = re[query]
            print(query)
            try:
                to = 'urmisatam2001@gmail.com'
                speak("What should the content ")
                content = takeCommand()
                

                sendEmail(to, content)
                print("Email has been sent" )
                speak("Email has been sent ")
            except Exception as e:
                
                print(e)
                print("sorry email faild to sent")
                speak("sorry email faild to sent") 
     
        elif "restart pc" in query:
            speak(" i am leaving and Restarting your pc")
            os.system("shutdown /r /t 1")
        
        elif "shutdown pc" in query:
            speak("Closing all running programs and system shuting down")
            os.system("shutdown /s /t 1 ")

        elif "jarvis are you listening me" in query:
            speak("yes")
            speak("sir i am waiting for your command")


        elif "leave" in query:
            speak("i am leaving sir...")
            speak("we will meet soon")
            
            exit()

