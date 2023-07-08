import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_command():
    try:
        with sr.Microphone() as source:
            talk("Hi guys ,i am your virtual assistant. how can i help you?")
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "youtube" in command:
                command = command.replace("youtube","")
    except:
        pass
    return command

def run_assistant():
    command = get_command()
    print(command)
    if 'play' in command:
        song = command.replace("play",' ')
        talk("playing"+ song)
        pywhatkit.playonyt(song)
        print("Playing songs")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H : %M %p")
        talk("Now time is "+ time)

    elif "tell me about" in command:
        about = command.replace("tell me about","")
        info = wikipedia.summary(about,3)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "thank you"or "ok" in command:
        talk("Thank you guys")
        exit()
    else:
        talk("sorry i can't understand tell me again")
while True:
    run_assistant()