import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import tempfile

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts = gTTS(text, lang='vi')
            tts.save(temp_audio_file.name)
            temp_audio_file.close()
            play_audio(temp_audio_file.name)
            os.remove(temp_audio_file.name)
            messagebox.showinfo("Thông báo", "Đã chuyển văn bản thành âm thanh tạm thời")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo âm thanh tạm thời: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản vào ô trống")

def play_audio(file_path):
    try:
        audio = AudioSegment.from_file(file_path, format="mp3")
        play(audio)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể phát âm thanh: {e}")

def save_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            try:
                tts = gTTS(text, lang='vi')
                tts.save(file_path)
                messagebox.showinfo("Thông báo", f"Đã lưu tệp âm thanh thành công: {file_path}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu tệp âm thanh: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản vào ô trống")

def preview_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts = gTTS(text, lang='vi')
            tts.save(temp_audio_file.name)
            temp_audio_file.close()
            play_audio(temp_audio_file.name)
            os.remove(temp_audio_file.name)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo âm thanh tạm thời: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản vào ô trống")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển văn bản thành âm thanh")
root.geometry("400x300")

# Tạo ô nhập văn bản
text_entry = tk.Text(root, height=10, width=50, font=("Arial", 12))
text_entry.pack(pady=10)

# Tạo nút nghe thử âm thanh tạm thời
convert_button = tk.Button(root, text="Nghe thử", command=preview_audio, font=("Arial", 14))
convert_button.pack(pady=5)

# Tạo nút lưu âm thanh dưới dạng MP3
save_button = tk.Button(root, text="Lưu thành MP3", command=save_audio, font=("Arial", 14))
save_button.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
