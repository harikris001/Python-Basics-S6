import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

photo = Image.open("image.png")
converted = ImageTk.PhotoImage(photo)

image_label = tk.Label(root,image=converted)

image_label.pack()

root.mainloop()