import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 400))  # Resize if needed
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk  # Keep a reference

# GUI setup
root = tk.Tk()
root.title("Image Viewer")

btn = tk.Button(root, text="Choose Image", command=open_image)
btn.pack(pady=10)

label = tk.Label(root)
label.pack()

root.mainloop()