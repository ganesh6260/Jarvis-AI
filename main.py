from voice.listen import listen
from voice.speak import speak


def main():
    print("========== JARVIS AI ==========")

    speak("Hello Ganesh.")
    speak("Please say something.")

    text = listen()

    if text:
        speak(f"You said {text}")


if __name__ == "__main__":
    main()