import whisper
import sounddevice as sd
import numpy as np
import queue

from gemini import ask_gemini
from tts import speak
from rag import retrieve_info

# Load model
model = whisper.load_model("medium")

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

print("🎤 Real-time assistant started... Speak Telugu")

samplerate = 16000

with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
    while True:
        audio_data = []
        
        # collect ~3 seconds audio
        for _ in range(0, int(samplerate / 1024 * 3)):
            audio_data.append(q.get())

        audio_np = np.concatenate(audio_data, axis=0)

        # save temp audio
        from scipy.io.wavfile import write
        write("temp.wav", samplerate, audio_np)

        # STT
        result = model.transcribe("temp.wav", language="te")
        user_text = result["text"].strip()

        if user_text:
            print("📝 మీరు:", user_text)

            # RAG
            rag_info = retrieve_info(user_text)

            # Gemini
            response = ask_gemini(user_text + "\n" + rag_info)
            print("🤖 AI:", response)

            # Speak
            speak(response)
