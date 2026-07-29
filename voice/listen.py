import tempfile
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


# Load Whisper model only once
model = WhisperModel("tiny", device="cpu", compute_type="int8")


def listen():
    """
    Record audio from microphone and convert it to text using Whisper.
    """

    samplerate = 16000
    duration = 5  # seconds

    print("🎤 Listening...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        sf.write(temp_audio.name, audio, samplerate)

        print("🔄 Recognizing...")

        segments, info = model.transcribe(temp_audio.name)

        text = " ".join(segment.text for segment in segments)

    print(f"You said: {text}")

    return text.lower()