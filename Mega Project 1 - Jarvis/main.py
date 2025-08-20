import speech_recognition as sr 
import webbrowser
import pyttsx3

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        print("recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
            
