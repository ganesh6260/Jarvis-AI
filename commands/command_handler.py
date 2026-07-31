import os
import webbrowser
from urllib.parse import quote
from datetime import datetime
from utils.system_utils import take_screenshot, save_note


def execute_command(command):
    command = command.lower().strip()

    # ---------- Exit ----------
    if any(word in command for word in ["exit", "bye", "goodbye"]):
        return "exit"

    # ---------- Open Websites ----------
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "linkedin": "https://www.linkedin.com",
        "gmail": "https://mail.google.com",
    }

    for name, url in websites.items():
        if f"open {name}" in command:
            webbrowser.open(url)
            return f"Opening {name.title()}."

    # ---------- Open macOS Apps ----------
    apps = {
        "chrome": "Google Chrome",
        "calculator": "Calculator",
        "finder": "Finder",
        "vs code": "Visual Studio Code",
        "vscode": "Visual Studio Code",
    }

    for keyword, app in apps.items():
        if f"open {keyword}" in command:
            os.system(f'open -a "{app}"')
            return f"Opening {app}."

    # ---------- Time ----------
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # ---------- Date ----------
    if "date" in command or "today" in command:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    # ---------- Day ----------
    if "what day" in command or "day is today" in command:
        today_day = datetime.now().strftime("%A")
        return f"Today is {today_day}."

    # ---------- Weather ----------
    if "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Opening Weather."
    
    # ---------- Screenshot ----------
    if "screenshot" in command:
        return take_screenshot()
    
    # ---------- Notes ----------
    if command.startswith("note "):
        note = command.replace("note ", "").strip()
        return save_note(note)

    # ---------- Google Search ----------
    if command.startswith("search "):
        query = command.replace("search ", "").strip()
        webbrowser.open(
            f"https://www.google.com/search?q={quote(query)}"
        )
        return f"Searching Google for {query}."

    if command.startswith("google "):
        query = command.replace("google ", "").strip()
        webbrowser.open(
            f"https://www.google.com/search?q={quote(query)}"
        )
        return f"Searching Google for {query}."

    # ---------- YouTube Search ----------
    if command.startswith("youtube "):
        query = command.replace("youtube ", "").strip()
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(query)}"
        )
        return f"Searching YouTube for {query}."

    # ---------- Play Music ----------
    if command.startswith("play "):
        query = command.replace("play ", "").strip()
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(query)}"
        )
        return f"Playing {query} on YouTube."

    return None