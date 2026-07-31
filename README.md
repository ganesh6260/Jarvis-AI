# 🤖 Jarvis AI — Desktop Voice Assistant

A Python-based desktop voice assistant inspired by JARVIS. It listens to your voice, executes local commands, and falls back to **Google Gemini** for open-ended questions it doesn't recognize. Comes with both a **CLI mode** and a **PySide6 GUI mode**.

> 🚧 Status: Under active development

---

## ✨ Features

- 🎙️ **Voice input** via `SpeechRecognition`
- 🔊 **Voice output (TTS)** via `pyttsx3`
- 🧠 **AI fallback** — unrecognized commands are answered using Google Gemini
- 💬 **Custom command handling** — extend it with your own commands
- 🖥️ **Two interfaces**:
  - `main.py` — simple command-line mode
  - `gui.py` — dark-themed desktop GUI with chat log, built with PySide6

---

## 📁 Project Structure

```
Jarvis-AI/
├── ai/              # Gemini API integration
├── commands/        # Command parsing & handling logic
├── voice/           # Speech-to-text (listen) and text-to-speech (speak)
├── utils/           # Helper utilities
├── config.py        # App configuration
├── gui.py           # PySide6 desktop GUI
├── main.py          # CLI entry point
├── requirements.txt # Python dependencies
└── .env.example     # Sample environment file
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

## 🛠️ Tech Stack

| Purpose            | Library              |
|---------------------|----------------------|
| Speech recognition  | `SpeechRecognition`  |
| Text-to-speech      | `pyttsx3`             |
| AI responses        | `google-generativeai` (Gemini) |
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

## 📌 Roadmap / Ideas

- [ ] Add more offline commands (system control, app launching, web search)
- [ ] Add unit tests for `commands/` and `ai/` modules
- [ ] Add wake-word detection instead of manual trigger
- [ ] Package as a standalone `.exe` for Windows

---

## 📄 License

This project currently has no license file. Consider adding one (e.g. MIT) if you want others to freely use/contribute to it.

---

## 🙋 Author

**Ganesh** — [@ganesh6260](https://github.com/ganesh6260)