import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    elif hour >= 16 and hour < 20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am your assistant shivam tell me  how can i help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "none"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'mypassword')
    server.sendmail('my email', to, content)
    server.close()


if __name__ == "__main__":
    speak("Hello shivam")
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("acording to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'how are you david' in query:
            speak("i m fine shivam what about you")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\mymusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time david' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open vs code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'what is your name' in query:
            speak("my name is david")
        elif 'good night' in query:
            speak("good night shivam")
        elif 'fine' in query:
            speak("what can i do for u shivam")
        elif 'good morning david' in query:
            speak("good morning shivam")
        elif 'thank you david' in query:
            speak("welcome shivam")
        elif 'email to shivam' in query:
            try:

                speak("what should i send")
                content = takecommand()
                to = "receiveremail@gmail.com"
                sendemail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry shivam i am not able to send this email")
