
import  pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import importlib
import cv2
import numpy as np
from multiprocessing import Process
import sys


engine = pyttsx3.init('sapi5')  #microsoft speech api
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id) #voices[0] is for male and voices[1] for  female
rate = engine.getProperty('rate')
engine.setProperty('rate',160)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishme():


    hour = int(datetime.datetime.now().hour)

    if (hour >= 0 and hour < 12):
        speak("good morning")

    elif (hour >= 12 and hour <= 18):
        speak("good evening")

    else:
        speak("good night")
    speak("welcome yash this is jarvis here  how can i help you ")


def jarvisanimaton():
    cap = cv2.VideoCapture('jarvisanimation.webm')

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame

            # Press Q on keyboard to  exit
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            cv2.imshow('Frame', frame)


        # Break the loop
        else:
            #cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

    # When everyhing done, release
    # the video capture object

    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

def takecommand():
    # it take input from user through microphone
     r = sr.Recognizer()  # recognizer class help to take recognize input from user
     with sr.Microphone() as source:
         print("Listening .....")
         speak("jarvis is listening please give command")
         r.pause_threshold = 1
         audio = r.listen(source)

     try:
         print("recognize ....")
         query = r.recognize_google(audio ,language="en-in")
         print(f"user said:{query}\n")

     except Exception as e:
         print("say that again ..")
         return "None"
     return query



def jarvis():
    cap = cv2.VideoCapture('jarvis.webm')

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Frame', frame)
            # Press Q on keyboard to  exit\
            cv2.waitKey(100)





        # Break the loop
        else:
            # cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

    # When everyhing done, release
    # the video capture object

    cap.release()
    cv2.destroyAllWindows()

    # Closes all the frames

def call():
    while True:

        query = takecommand().lower()  # convert query in lower case

        if ('wikipedia' in query):
            speak('searching wikipedia')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            speak(result)
            print(result)

        elif ('youtube' in query):
            webbrowser.open("youtube.com")

        elif ('open images' in query):
            image_dir = 'C:\\Users\\yash\\Pictures\\Screenshots'
            images = os.listdir(image_dir)
            print(images)
            os.startfile(os.path.join(image_dir, images))

        elif ('time' in query):
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)

        elif ('sublime' in query):
            sublime = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublime)

        elif ('open chrome' in query):
            chrome = "C:\\Users\\yash\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)

        elif ("jarvis quit" in query):
            exit()


if __name__ == "__main__":

    p1 = Process(target=wishme)
    p1.start()
    p2 = Process(target=jarvisanimaton)
    p2.start()
    # This is where I had to add the join() function.
    p1.join()
    p2.join()

    p3 = Process(target=jarvis)
    p3.start()
    p4 = Process(target=call)
    p4.start()
    # This is where I had to add the join() function.
    p3.join()
    p4.join()


