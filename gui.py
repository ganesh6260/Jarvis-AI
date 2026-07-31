import sys
import threading

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from datetime import datetime

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
        self.status.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#00ff66;
        """)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.button = QPushButton("🎤 TALK TO JARVIS")
        self.button.clicked.connect(self.start_listening)

        self.clear_btn = QPushButton("🧹 Clear Chat")
        self.clear_btn.clicked.connect(self.chat.clear)

        buttons = QHBoxLayout()
        buttons.addWidget(self.button)
        buttons.addWidget(self.clear_btn)

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.chat)
        layout.addLayout(buttons)

        self.setLayout(layout)

    def log(self, text):
        now = datetime.now().strftime("%H:%M:%S")

        self.chat.append(f"[{now}] {text}")

        scrollbar = self.chat.verticalScrollBar()

        scrollbar.setValue(scrollbar.maximum())

    def start_listening(self):
        thread = threading.Thread(target=self.run_jarvis)
        thread.daemon = True
        thread.start()

    def run_jarvis(self):
        self.button.setEnabled(False)
        self.status.setText("🟡 Listening...")
        self.status.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#FFD700;
        """)

        command = listen()
  
        if not command:
            self.status.setText("🟢 Ready")
            self.status.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:#00ff66;
            """)
            self.button.setEnabled(True)
            return

        self.log(f"🧑 You : {command}")

        response = execute_command(command)

        if response == "exit":

            self.log("🤖 Jarvis : Goodbye!")
            speak("Goodbye Ganesh")
            
            self.button.setEnabled(True)
            QApplication.quit()
            return

        if response:

            self.log(f"🤖 Jarvis : {response}")
            speak(response)

        else:
            self.status.setText("🔵 Thinking...")
            self.status.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:#4da6ff;
            """)
            try:
                answer = ask_gemini(command)

            except Exception:
                answer = (
                    "⚠️ Gemini quota reached.\n"
                    "Offline commands are still available."
                )

            self.log(f"🤖 Jarvis : {answer}")
            speak(answer)

        self.status.setText("🟢 Ready")
        self.status.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#00ff66;
        """)
        self.button.setEnabled(True)


app = QApplication(sys.argv)

window = JarvisGUI()

window.show()

sys.exit(app.exec())