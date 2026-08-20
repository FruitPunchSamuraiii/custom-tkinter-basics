from tkinter import *
import customtkinter

root = customtkinter.CTk()

def colour_picker(choice):
    my_label.configure(text=choice, text_color=choice)

def colour_picker2():
    my_label.configure(text=my_option.get(), text_color=my_option.get())

def yellow():
    my_option.set("Yellow")
    my_label.configure(text=my_option.get(), text_color=my_option.get())


#Set the options for our optionmenu
colours = ["Red", "Green", "Blue"]

#Creat OptionMenu
my_option = customtkinter.CTkOptionMenu(root, values=colours,) #combobox you can type but option menu can't
                                        #command=colour_picker)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

pick_button = customtkinter.CTkButton(root, text="Make choice", 
                                      command=colour_picker2)
pick_button.pack(pady=10)

yellow_button = customtkinter.CTkButton(root, text="Yellow button", command=yellow)
yellow_button.pack(pady=10)
root.mainloop()