import time

from voice.speak import speak
from voice.listen import listen

from commands.command_handler import execute_command
from ai.gemini import ask_gemini


def main():

    print("=" * 10, "JARVIS AI", "=" * 10)

    speak("Hello Ganesh.")

    while True:

        speak("Please say a command.")

        time.sleep(2)

        command = listen()

        if not command:
            continue

        response = execute_command(command)

        if response == "exit":
            speak("Goodbye Ganesh.")
            break

        if response:
            speak(response)

        else:
            ai_response = ask_gemini(command)
            speak(ai_response)


if __name__ == "__main__":
    main()