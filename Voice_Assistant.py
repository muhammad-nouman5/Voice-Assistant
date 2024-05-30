import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You Said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
    except sr.RequestError as e:
        print("Sorry, error in retrieving audio: ", str(e))

    return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant said: ", text)

speak("Hello! How can I assist you?")

while True:
    command = listen()
    if "hello" in command.lower():
        speak("Hello! How can I assist you?")
    elif "goodbye" in command.lower():
        speak("Good Bye!")
        break
    elif "what's your name" in command.lower():
        speak("My name is Voice Assistant")
    elif "tell me a joke" in command.lower():
        speak("Hey, here's your joke of the day")
    elif "how is the weather" in command.lower():
        speak("It's very hot and sunny today")
    else:
        speak("Sorry! I don't know how to respond")
