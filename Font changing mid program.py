from tkinter import *
import customtkinter

root = customtkinter.CTk()

def change():
    my_font.configure(underline=False, overstrike=False, size=22, slant="italic")

my_font = customtkinter.CTkFont(family="Arial", size=40, 
                                weight="bold", #bold/normal
                                slant="roman", # roman is up and down, you can also do italic
                                underline=True,
                                overstrike=True
                                )

my_label = customtkinter.CTkLabel(root, text="This is text",
                                    font = my_font
                                  )
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Change text", command=change)
my_button.pack(pady=20)

root.mainloop()