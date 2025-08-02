import whisper
import cohere
import pyttsx3

# 1. تحويل الصوت إلى نص باستخدام Whisper
def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

# 2. إرسال النص إلى Cohere (مع دعم العربية)
def generate_response(text, cohere_api_key):
    co = cohere.Client(cohere_api_key)
    response = co.generate(
        model='command',
        prompt=text + "\nالرجاء الرد باللغة العربية.",
        max_tokens=200
    )
    return response.generations[0].text.strip()

# 3. تحويل النص إلى صوت باستخدام pyttsx3
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    # تقسيم النص الطويل إلى جمل
    sentences = text.split('. ')
    for sentence in sentences:
        if sentence.strip():  # تجاهل الفراغات
            engine.say(sentence.strip())
    engine.runAndWait()

# --------- التشغيل الرئيسي ---------
if __name__ == "__main__":
    audio_file = "hi there.mp3"  # تأكد أن الملف موجود في نفس المجلد
    cohere_api_key = "6tD3ceNUpTTV8C7QsFZDOWCEIlPGCWldlwZKoR8"

    print("🎧 جاري تحويل الصوت إلى نص...")
    text = transcribe_audio(audio_file)
    print("📝 النص المستخرج:", text)

    print("🧠 جاري توليد الرد من Cohere...")
    reply = generate_response(text, cohere_api_key)
    print("🤖 رد النموذج:", reply)

    print("🔊 جاري تشغيل الرد صوتيًا...")

    speak_text(reply)
