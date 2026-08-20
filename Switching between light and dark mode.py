from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")#you cant change the theme programatically, you have to hard code it


root = customtkinter.CTk()

mode = "dark"

def change_colors(choice):
    customtkinter.set_default_color_theme(choice)

def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        #Clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "This is light mode...")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        my_text.delete(0.0, END)
        my_text.insert(END, "This is dark mode...")

my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)
my_button.pack(pady=20)

#colors = ["blue", "dark-blue", "green", "purple"]
#my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors)

root.mainloop()