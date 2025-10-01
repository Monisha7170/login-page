import tkinter as tk
from tkinter import messagebox
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()


def login():
    username = username_entry.get()
    password = password_entry.get()

    
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        speak(f"Welcome {username}, login successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")
        speak("Invalid username or password, please try again!")


root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.config(bg="#E6E6FA")  


tk.Label(root, text="Login Page", font=("Arial", 18, "bold"), bg="#E6E6FA").pack(pady=10)


tk.Label(root, text="Username:", font=("Arial", 12), bg="#E6E6FA").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)


tk.Label(root, text="Password:", font=("Arial", 12), bg="#E6E6FA").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)


tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="#9370DB", fg="white", command=login).pack(pady=20)


root.mainloop()
