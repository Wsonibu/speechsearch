import speech_recognition as sr
import webbrowser

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Đang lắng nghe...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="vi-VN")
        print(f"Bạn đã nói: {text}")
        return text
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói")
    except sr.RequestError:
        print("Không thể kết nối tới dịch vụ nhận dạng giọng nói")

    return None

def search_on_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    text = recognize_speech()
    if text:
        search_on_google(text)
