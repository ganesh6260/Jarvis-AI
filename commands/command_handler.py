import webbrowser


def execute_command(command):
    command = command.lower()

    if "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    elif "exit" in command or "bye" in command:
        return "exit"

    return None