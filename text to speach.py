import pyttsx3

def speak_text(text, voice_choice='female'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')

    if voice_choice.lower() == 'male':
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)   

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to speak: ")
    choice = input("Choose voice (male/female): ").strip().lower()
    speak_text(text, voice_choice=choice)
