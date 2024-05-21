from assistant.listener import listen
from assistant.responder import respond
from assistant.search import search_and_respond

def main():
    print("Halo, saya AI Dicky. Bagaimana saya bisa membantu Anda hari ini?")
    while True:
        try:
            text = listen()
            if "cari" in text.lower():
                search_and_respond(text)
            else:
                respond(text)
        except KeyboardInterrupt:
            print("Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
