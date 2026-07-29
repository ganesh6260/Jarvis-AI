import speech_recognition as sr


def listen():
    """
    Listen from the microphone and convert speech to text.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("🔄 Recognizing...")

        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError as e:
        print(f"Speech Recognition Error: {e}")
        return ""