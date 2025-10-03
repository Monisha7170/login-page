import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

def play_video():
    # Open file chooser
    file_path = filedialog.askopenfilename(
        title="Select a video",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
    )

    if not file_path:
        return  # Exit if no video selected

    cap = cv2.VideoCapture(file_path)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((640, 480))
            imgtk = ImageTk.PhotoImage(image=img)
            lbl.imgtk = imgtk
            lbl.config(image=imgtk)
            lbl.after(10, update_frame)
        else:
            cap.release()

    update_frame()

# GUI setup
root = tk.Tk()
root.title("Video Player")

btn = tk.Button(root, text="Choose and Play Video", command=play_video)
btn.pack(pady=10)

lbl = tk.Label(root)
lbl.pack()

root.mainloop()
