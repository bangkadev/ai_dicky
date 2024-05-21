from gtts import gTTS
import playsound
import os
import openai

# Masukkan API Key OpenAI Anda di sini
openai.api_key = 'Masukkan Kunci Api Anda'

def respond(text):
    if text:
        response_text = get_openai_response(text)
        if response_text:
            speak(response_text)
        else:
            speak("Maaf, saya tidak punya jawaban untuk itu.")

def speak(text):
    tts = gTTS(text=text, lang='id')
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )
        # Mengakses konten pesan dari respon OpenAI
        return response.choices[0]['message']['content'].strip()
    except openai.error.RateLimitError as e:
        # Penanganan khusus untuk kesalahan kuota terlampaui
        print("Kuota API terlampaui. Silakan cek rencana dan detail penagihan Anda.")
    except Exception as e:
        # Menampilkan pesan error jika terjadi kesalahan umum lainnya
        print(f"Error mendapatkan respon dari OpenAI: {e}")
    return ""
