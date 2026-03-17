import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    if __name__ == "__main__":
        text_to_speak = input("Enter the text you want to speak: ")
        speak(text_to_speak)
