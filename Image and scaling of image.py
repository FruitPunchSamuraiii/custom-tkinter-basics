from tkinter import *
import customtkinter
from PIL import Image

root = customtkinter.CTk()

my_image = customtkinter.CTkImage(
    light_image=Image.open(r'D:\newdownload\silly.png'),
    dark_image=Image.open(r'D:\newdownload\silly.png'),
    size=(360, 500)  # <--- Change image size here (width, height)
)

my_label = customtkinter.CTkLabel(
    root, 
    text="", 
    image=my_image #you can my_image.configure(size=(400, 400)) to change the size dynamically
)
my_label.pack(pady=20)

root.mainloop()