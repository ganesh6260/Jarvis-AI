# 🤖 Jarvis AI — Desktop Voice Assistant

A Python-based desktop voice assistant inspired by JARVIS. It listens to your voice, executes local commands, and falls back to **Google Gemini** for open-ended questions it doesn't recognize. Comes with both a **CLI mode** and a **PySide6 GUI mode**.

> ✅ Current Version: v1.0 (Voice Assistant with GUI & AI Integration)

---

## ✨ Features

- 🎙️ Voice input using SpeechRecognition
- 🔊 Text-to-Speech using pyttsx3
- 🤖 AI responses using Google Gemini
- 🌐 Open websites (Google, YouTube, GitHub, Gmail, LinkedIn)
- 💻 Launch desktop applications
- 🔎 Google & YouTube search using voice
- 📸 Take screenshots using voice command
- 📝 Save notes using voice
- ⏰ Tell current time and date
- 🖥️ Modern PySide6 GUI
- 💬 CLI Mode + GUI Mode
---

## 📁 Project Structure

```text
Jarvis-AI/
│
├── ai/
│   ├── __init__.py
│   └── gemini.py              # Google Gemini AI integration
│
├── commands/
│   ├── __init__.py
│   └── command_handler.py     # Voice command processing
│
├── voice/
│   ├── __init__.py
│   ├── listen.py              # Speech Recognition
│   └── speak.py               # Text-to-Speech
│
├── utils/
│   ├── __init__.py
│   └── system_utils.py        # Screenshot & Notes utilities
│
├── gui.py                     # PySide6 Desktop GUI
├── main.py                    # Command Line Version
├── config.py                  # Application configuration
├── requirements.txt           # Project dependencies
├── .env.example               # Gemini API Key example
├── .gitignore
└── README.md
```
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ganesh6260/Jarvis-AI.git
cd Jarvis-AI
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Note (Windows users):** If `PyAudio` fails to install, download a precompiled wheel from [gohlke's PyAudio builds](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
> ```bash
> pip install PyAudio‑<version>‑cp3xx‑cp3xx‑win_amd64.whl
> ```

### 4. Set up your environment variables

Copy `.env.example` to `.env` and add your own Gemini API key:

```bash
cp .env.example .env
```

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the assistant

**CLI mode:**
```bash
python main.py
```

**GUI mode:**
```bash
python gui.py
```

---

## 🗣️ Usage

- Once running, say **"Please say a command"** prompt will appear (CLI) or click **🎤 TALK TO JARVIS** (GUI).
- Speak a known command (e.g. open an app, tell the time, etc. — depending on what's implemented in `commands/command_handler.py`).
- If the command isn't recognized locally, Jarvis will send it to **Gemini** and speak back the AI-generated response.
- Say **"exit"** to close the assistant.

---
### Supported Voice Commands

- Open Google
- Open YouTube
- Open GitHub
- Open Gmail
- Open Chrome
- Open Calculator
- Search Python tutorial
- Google Machine Learning
- Play Arijit Singh songs
- Take Screenshot
- Save Note
- What is the time?
- What day is today?
- Exit

---

## 🛠️ Tech Stack

| Purpose            | Library              |
|---------------------|----------------------|
| Speech recognition  | `SpeechRecognition`  |
| Text-to-speech      | `pyttsx3`             |
| AI Responses        | Google GenAI SDK |
| GUI                 | `PySide6`             |
| Config management   | `python-dotenv`       |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📌 Future Improvements

- [ ] Weather information
- [ ] Email sending
- [ ] WhatsApp messaging
- [ ] AI memory (conversation history)
- [ ] Smart wake word detection ("Hey Jarvis")
- [ ] Cross-platform packaging
---

## 📄 License

This project currently has no license file. Consider adding one (e.g. MIT) if you want others to freely use/contribute to it.

---

## 👨‍💻 Author

Ganesh Patel

MCA (AI & IoT)
National Institute of Technology Patna

GitHub:
https://github.com/ganesh6260