import speech_recognition as sr #pip install speechRecognition
import pyttsx3 #pip install pyttsx3
import wikipedia #pip install wikipedia
import pywhatkit #pip install pywhatkit
import pyjokes #pip install pyjokes
import datetime
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir Please tell me how may I help you")       

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print("Recognizing...")
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

if __name__ == "__main__":
    wishMe()
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'are you single' in command:
            talk('I am in a relationship with wifi')

        elif 'joke' in command:
            talk(pyjokes.get_joke())
        
        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")   

        else:
            talk('Please say the command again.')

