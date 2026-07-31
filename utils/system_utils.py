import os
from datetime import datetime
import pyautogui


def take_screenshot():
    """
    Takes a screenshot and saves it in the assets folder.
    """

    os.makedirs("assets", exist_ok=True)

    filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")

    filepath = os.path.join("assets", filename)

    screenshot = pyautogui.screenshot()

    screenshot.save(filepath)

    return f"Screenshot saved as {filename}."


def save_note(note):
    """
    Saves a note into assets/notes.txt
    """

    os.makedirs("assets", exist_ok=True)

    filepath = os.path.join("assets", "notes.txt")

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()}\n")
        file.write(note + "\n")
        file.write("-" * 50 + "\n")

    return "Your note has been saved."