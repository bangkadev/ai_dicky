import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="id-ID")
        print(f"Anda berkata: {text}")
        return text
    except sr.UnknownValueError:
        print("Maaf, saya tidak mengerti.")
        return ""
    except sr.RequestError as e:
        print(f"Tidak dapat meminta hasil; {e}")
        return ""
