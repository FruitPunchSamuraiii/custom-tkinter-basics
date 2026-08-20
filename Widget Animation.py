from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry('700x450')

global my_y
my_y= 750/2+350

def up():
    global my_y
    my_y -= 20
    if my_y >=195:
        my_text.place(x=700/2,y=my_y,anchor='center')
        up_button.configure(text=my_y)
        root.after(10, up)

def down():
    global my_y
    my_y += 20
    if my_y <=750: #you can do the x axis to go the other way
        my_text.place(x=700/2,y=my_y,anchor='center')
        down_button.configure(text=my_y)
        root.after(10, down) #1 second is 1000

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=20)

up_button = customtkinter.CTkButton(my_frame, text="Up", command=up)
up_button.grid(row=0, column=0, padx=10)

down_button = customtkinter.CTkButton(my_frame, text="Down", command=down)
down_button.grid(row=0, column=1, padx=10)

my_text = customtkinter.CTkTextbox(root, width=400, height=200)
my_text.place(x=700/2,y=my_y,anchor='center')

root.mainloop()