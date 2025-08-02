# 🎙️ AI Voice Assistant – Whisper + Cohere + TTS

This project is a simple voice assistant pipeline that:

1. 🎧 Converts voice input to text using OpenAI Whisper
2. 🧠 Sends the transcribed text to Cohere LLM to generate a smart response (in Arabic)
3. 🔊 Converts the AI response to spoken voice using pyttsx3

---

## 🚀 Features

- 🎤 Input: Audio file (`.mp3`)
- 📝 Transcription: Done using Whisper (`base` model)
- 🧠 Smart reply: Generated via Cohere's LLM (supports Arabic)
- 🔊 TTS output: Uses pyttsx3 to read the reply aloud
- 💡 Fully scriptable and modifiable for your own AI voice assistant

---

## 📦 Requirements

Install required packages using pip:
pip install openai-whisper
pip install cohere
pip install pyttsx3

> ✅ Make sure your system has Python 3.10 or 3.12 (avoid Anaconda if facing audio issues).

---

## 📁 File Structure
project/
│
├── AI.py                # Main Python script
├── hi there.mp3         # Example input audio file
├── README.md            # Project description

---

## 🔧 How It Works

### 1. 🎧 Speech Recognition via Whisper

The script loads a Whisper model and transcribes the audio:
model = whisper.load_model("base")
result = model.transcribe(file_path)

### 2. 🧠 Response Generation via Cohere

The text is sent to Cohere for Arabic-language reply generation:
response = co.generate(
    model='command',
    prompt=text + "\nالرجاء الرد باللغة العربية.",
    max_tokens=200
)

### 3. 🔊 Text-to-Speech via pyttsx3

The AI-generated response is spoken aloud:
engine.say(sentence)
engine.runAndWait()

---

## 🧪 Usage

### 1. Place your audio file (e.g., `hi there.mp3`) in the same folder as the script.

### 2. Open a terminal and run:
python AI.py

You should see:
- Transcribed text printed
- AI response in Arabic
- Audio response played through speakers

---
