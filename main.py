from voice.speak import speak
from voice.listen import listen
from commands.command_handler import execute_command
import time


def main():
    print("========== JARVIS AI ==========")

    speak("Hello Ganesh.")
    speak("Please say a command.")

    time.sleep(2)

    command = listen()

    if command:
        response = execute_command(command)

        if response == "exit":
            speak("Goodbye!")
            return

        speak(response)


if __name__ == "__main__":
    main()