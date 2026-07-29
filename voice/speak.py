import pyttsx3

# Create the text-to-speech engine
engine = pyttsx3.init()

# Configure voice settings
engine.setProperty("rate", 170)   # Speed
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)


def speak(text):
    """
    Convert text into speech.
    """
    print(f"Jarvis: {text}")

    engine.say(text)
    engine.runAndWait()