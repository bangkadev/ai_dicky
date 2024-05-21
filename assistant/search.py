import requests
from googlesearch import search
from bs4 import BeautifulSoup
from gtts import gTTS
import playsound
import os

def search_and_respond(query):
    try:
        search_results = search(query, num_results=5, lang="id")
        for result in search_results:
            response_text = get_text_from_url(result)
            if response_text:
                speak(response_text)
                return
        speak("Maaf, saya tidak menemukan informasi yang relevan.")
    except Exception as e:
        print(f"Error dalam pencarian: {e}")
        speak("Terjadi kesalahan saat mencari informasi.")

def get_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])
        return text[:500]  # Batasi jumlah karakter agar tidak terlalu panjang
    except Exception as e:
        print(f"Error mengambil konten dari {url}: {e}")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='id')
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
