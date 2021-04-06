import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()

engine=ts.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('listining...')
            talk("listening ...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            

    except:
        pass

    return command

def run_alexa():
    command=talk_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
        
    elif 'search for' in command:
        person=command.replace('search for','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
        print("thank you")
        talk("thank you")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("sorry I can't hear you")
        run_alexa()    
run_alexa()



