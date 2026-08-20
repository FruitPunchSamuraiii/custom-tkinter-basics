from tkinter import *
import customtkinter

root = customtkinter.CTk()

#Function
def input():
    dialog = customtkinter.CTkInputDialog(text="What is your name?", title="Hello :)",
                                            fg_color="orange",
                                            button_fg_color="red",
                                            button_hover_color="yellow",
                                            button_text_color="Black",
                                            entry_fg_color="Green",
                                            entry_border_color="Gray",
                                            text_color="Black",
                                            entry_text_color="Black"
                                          )
    thing = dialog.get_input() # you dont need to make it a variable but it is neater
    if thing:
        my_label.configure(text=f"Hello {thing}")
    else:
        my_label.configure(text="You forgot to type anything")

#Button
my_button = customtkinter.CTkButton(root, text="Click me", command=input)
my_button.pack(pady=40)

#Creat a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

root.mainloop()