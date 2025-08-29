import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import pyperclip

def generate_password():
    length = int(length_var.get())
    chars = ''
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_lower.get():
        chars += string.ascii_lowercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Error", "Please select at least one option.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

password_var = tk.StringVar()
length_var = tk.IntVar(value=12)
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

entry = ttk.Entry(root, textvariable=password_var, font=("Courier", 14), justify="center", state="readonly", width=30)
entry.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

ttk.Button(btn_frame, text="🔁 ReNew", command=generate_password).pack(side="left", padx=5)
ttk.Button(btn_frame, text="📋 Copy", command=copy_password).pack(side="left", padx=5)

ttk.Label(root, text="Password Length:").pack(pady=(15, 0))
slider = ttk.Scale(root, from_=6, to=32, variable=length_var, orient="horizontal")
slider.pack(fill="x", padx=20)

check_frame = tk.Frame(root)
check_frame.pack(pady=10)

ttk.Checkbutton(check_frame, text="Capital letters (A-Z)", variable=use_upper).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(check_frame, text="Lowercase letters (a-z)", variable=use_lower).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(check_frame, text="Numbers (0-9)", variable=use_digits).grid(row=0, column=1, sticky="w")
ttk.Checkbutton(check_frame, text="Symbols (!@#...)", variable=use_symbols).grid(row=1, column=1, sticky="w")

generate_password()

root.mainloop()