import pyttsx3
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import flask
import os
import cv2
import wikipedia
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 170)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=50, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    elif hour > 17 and hour<=20:
        speak("Good Evening")
    else:
        speak("Hello!")
    speak(" yo! sparky is here I am your Virtual Assistant please tell me how can i help you  ")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # opening basic application

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("opening notepad")

        elif "open command prompt" in query:
            os.system("Start cmd")
            speak("opening command prompt")

        elif "open camera" in query:
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()

                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        # open apps websites
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif "open github" in query:
            speak("opening github")
            webbrowser.open("https://github.com/Raj305173")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        #Common talk
        elif 'hai' in query or "hello" in query:
            speak("Yo whats up ")
        elif 'nothing much' in query or "bore" in query:
            speak(" ohk do you like to listening song or joke? ")
        elif 'what is your favourite food' in query:
            speak('i love pizza and paneer kulcha and yours?')


        elif 'pasta' in query or "sandwich" in query:
            speak("ohk nice ")
        elif 'paneer kulcha' in query or "my favorite food is pizza" in query:
            speak("we have similar test ")

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'who are you' in query:
            speak('I am a sparky assistent robot made by sneh')

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me by any name, but i am a friendly Virtual Assistant")

        elif "who is your Owner" in query or "who created you" in query:
            speak("I have been created by Sneh Agrawal.")

        #Open commands
        elif "open google" in query:
            speak("what should i search for you")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening ")
            speak(cm)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            print(song)
            pywhatkit.playonyt(song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'who is the' in query:
            person = query.replace('who is the', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        elif 'date' in query:
            hour = int(datetime.datetime.now().hour)
            print(hour)
            speak(hour)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #help for use

        elif "help" in query:
            speak("i can be very useful and easy to use")
            speak(" just say whatever you want me to search on google or play music or time & date information ")

            # stopping the program

        elif "shutdown" in query:
            speak("Have a good day!, Sir")
            sys.exit()
        elif "bye" in query:
            speak("bye!, Sir")
            sys.exit()
        else:
            speak("sorry i dont understand")