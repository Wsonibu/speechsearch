import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyautogui
import time

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

def type_text():
    text = recognize_speech()
    if text:
        time.sleep(1)  # Đợi một chút để đảm bảo con trỏ chuột ở đúng vị trí
        pyautogui.write(text, interval=0.1)
        messagebox.showinfo("Thông báo", "Đã nhập văn bản vào ô tìm kiếm:\n" + text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhập văn bản bằng giọng nói")
root.geometry("300x200")

# Tạo nút "Nói"
speak_button = tk.Button(root, text="Nói", command=type_text, font=("Arial", 14))
speak_button.pack(expand=True)

# Chạy ứng dụng
root.mainloop()
