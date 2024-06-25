import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyperclip

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        messagebox.showinfo("Thông báo", "Đang lắng nghe...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="vi-VN")
        print(f"Bạn đã nói: {text}")
        return text
    except sr.UnknownValueError:
        messagebox.showerror("Lỗi", "Không thể nhận dạng giọng nói")
    except sr.RequestError:
        messagebox.showerror("Lỗi", "Không thể kết nối tới dịch vụ nhận dạng giọng nói")

    return None

def copy_text():
    text = recognize_speech()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Thông báo", "Đã sao chép vào clipboard:\n" + text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Sao chép bằng giọng nói")
root.geometry("300x200")

# Tạo nút "Nói"
speak_button = tk.Button(root, text="Nói", command=copy_text, font=("Arial", 14))
speak_button.pack(expand=True)

# Chạy ứng dụng
root.mainloop()
