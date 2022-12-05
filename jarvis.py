import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you")


def takeCommand():
    #     It takes microphone input from the user and return s string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: ",query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jatinjain.cse23@jecrc.ac.in', 'jjcse@eng')
    server.sendmail('jatinjain.cse23@jecrc.ac.in',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")
        

        elif 'play music' in query:
            music_dir = 'C:\\Users\\jatin\\Desktop\\python\\Projects\\Jarvis\\Songs for me'
            songs = os.listdir(music_dir)
            a = random.randint(1,14)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\jatin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to jatin' in query:
            try:
                speak("What should I say: ")
                content = takeCommand()
                to = "18109457j@gmail.com"
                sendEmail(to,content)
                speak("Email has bean sent! ")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")
                
        elif 'quit' in query:
            exit()






    
