from tkinter import *
import customtkinter

root = customtkinter.CTk()

def new_window_creator():
    new_window = customtkinter.CTkToplevel(root, fg_color="black") #Creates a top level window
    new_window.title("New window made :)")
    new_window.geometry("400x200")
    new_window.resizable(False, False) # width and height made unable to resizeable

    def close():
        new_window.destroy()
        new_window.update()

    #Close the window through a button
    new_button = customtkinter.CTkButton(new_window, text="Close Window", command=close)
    new_button.pack(pady=40)


my_button = customtkinter.CTkButton(root, text="Open new window", command = new_window_creator) 
my_button.pack(pady=40)

root.mainloop()