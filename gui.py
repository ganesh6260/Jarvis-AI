import sys
import threading

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QVBoxLayout,
)

from voice.listen import listen
from voice.speak import speak
from commands.command_handler import execute_command
from ai.gemini import ask_gemini


class JarvisGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🤖 Jarvis AI Assistant")
        self.resize(700, 500)

        self.setStyleSheet("""
        QWidget{
            background-color:#1e1e2e;
            color:white;
            font-size:15px;
        }

        QTextEdit{
            background:#2b2d42;
            border-radius:10px;
            padding:10px;
            color:white;
        }

        QPushButton{
            background:#4CAF50;
            color:white;
            border:none;
            border-radius:10px;
            padding:12px;
            font-size:16px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#45a049;
        }

        QLabel{
            color:white;
        }
        """)

        self.title = QLabel("🤖 JARVIS AI ASSISTANT")
        self.title.setStyleSheet("""
            font-size:34px;
            font-weight:800;
            padding:15px;
        """)
  
        self.status = QLabel("🟢 Ready")

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.button = QPushButton("🎙️ TALK TO JARVIS")
        self.button.clicked.connect(self.start_listening)

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.chat)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def log(self, text):
        self.chat.append(text)

    def start_listening(self):
        thread = threading.Thread(target=self.run_jarvis)
        thread.daemon = True
        thread.start()

    def run_jarvis(self):

        self.status.setText("Status : Listening...")

        command = listen()

        if not command:
            self.status.setText("Status : Ready")
            return

        self.log(f"You : {command}")

        response = execute_command(command)

        if response == "exit":

            self.log("Jarvis : Goodbye!")
            speak("Goodbye Ganesh")

            QApplication.quit()
            return

        if response:

            self.log(f"Jarvis : {response}")
            speak(response)

        else:

            self.status.setText("Status : Thinking...")

            answer = ask_gemini(command)

            self.log(f"Jarvis : {answer}")

            speak(answer)

        self.status.setText("Status : Ready")


app = QApplication(sys.argv)

window = JarvisGUI()

window.show()

sys.exit(app.exec())