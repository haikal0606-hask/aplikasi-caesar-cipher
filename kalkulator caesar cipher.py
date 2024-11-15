import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    shift = int(shift)
    if mode == "Dekripsi":
        shift = -shift
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            result += shifted_char.upper() if char.isupper() else shifted_char
        else:
            result += char
    return result

def process():
    text = entry_text.get("1.0", tk.END).strip()
    shift = entry_shift.get()
    mode = mode_var.get()

    if not text or not shift.isdigit():
        messagebox.showerror("Kesalahan Input", "Masukkan teks dan nilai pergeseran yang valid!")
        return
    
    result = caesar_cipher(text, int(shift), mode)
    result_text.set(result)

def clear_fields():
    entry_text.delete("1.0", tk.END)
    entry_shift.delete(0, tk.END)
    result_text.set("")

# GUI Setup
app = tk.Tk()
app.title("Caesar Cipher - Enkripsi dan Dekripsi")
app.geometry("600x500")
app.configure(bg="#34495E")

# Style Configuration
style = ttk.Style()
style.configure('TFrame', background='#34495E')
style.configure('TLabel', background='#34495E', foreground='white', font=('Helvetica', 14))
style.configure('TButton', font=('Helvetica', 12, 'bold'))

# Text Label and Entry
frame_text = ttk.Frame(app)
frame_text.pack(pady=20, padx=20, fill="x")
ttk.Label(frame_text, text="Masukkan Teks:").pack(anchor="w", padx=10, pady=5)
entry_text = tk.Text(frame_text, height=5, font=("Helvetica", 12), bg="#ECF0F1", wrap="word")
entry_text.pack(padx=10, pady=5, fill="x")

# Shift Label and Entry
frame_shift = ttk.Frame(app)
frame_shift.pack(pady=10, padx=20, fill="x")
ttk.Label(frame_shift, text="Masukkan Pergeseran (angka):").pack(anchor="w", padx=10, pady=5)
entry_shift = ttk.Entry(frame_shift, font=("Helvetica", 12))
entry_shift.pack(padx=10, pady=5, fill="x")

# Mode Selection
frame_mode = ttk.Frame(app)
frame_mode.pack(pady=10, padx=20, fill="x")
mode_var = tk.StringVar(value="Enkripsi")
ttk.Label(frame_mode, text="Pilih Mode:").pack(anchor="w", padx=10, pady=5)
ttk.Radiobutton(frame_mode, text="Enkripsi", variable=mode_var, value="Enkripsi").pack(anchor="w", padx=30)
ttk.Radiobutton(frame_mode, text="Dekripsi", variable=mode_var, value="Dekripsi").pack(anchor="w", padx=30)

# Result Display
frame_result = ttk.Frame(app)
frame_result.pack(pady=10, padx=20, fill="x")
result_text = tk.StringVar()
ttk.Label(frame_result, text="Hasil:").pack(anchor="w", padx=10, pady=5)
ttk.Entry(frame_result, textvariable=result_text, state="readonly", font=("Helvetica", 12), background="#ECF0F1").pack(padx=10, pady=5, fill="x")

# Buttons
button_frame = ttk.Frame(app)
button_frame.pack(pady=20, padx=20, fill="x")

tk.Button(button_frame, text="Proses", command=process, bg='#1ABC9C', fg='white', font=('Helvetica', 12, 'bold')).pack(side="left", padx=10, pady=5, expand=True)
tk.Button(button_frame, text="Bersihkan", command=clear_fields, bg='#3498DB', fg='white', font=('Helvetica', 12, 'bold')).pack(side="left", padx=10, pady=5, expand=True)
tk.Button(button_frame, text="Keluar", command=app.quit, bg='#E74C3C', fg='white', font=('Helvetica', 12, 'bold')).pack(side="left", padx=10, pady=5, expand=True)

# Run the application
app.mainloop()