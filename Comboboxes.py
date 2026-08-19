from tkinter import *
import customtkinter

root = customtkinter.CTk()

def colour_picker(choice):
    my_label.configure(text=f"You picked {choice}")

def colour_picker2():
    my_label.configure(text=my_combobox.get(), text_color=my_combobox.get()) #changes the text of the label to the colour you picked, and changes the colour of the text to that colour

def colour_picker_red():
    #set combo box to red
    my_combobox.set("Red") # you can make this even something not even an option in the combobox, but it will still work
    my_label.configure(text="You picked Red", text_color="red") #changes the text of the label to red, and changes the colour of the text to red


my_label = customtkinter.CTkLabel(root, text="Pick a colour")
my_label.pack(pady=40)

#create combobox with colours
colours = ["Red", "Green", "Blue", "Yellow"]
my_combobox = customtkinter.CTkComboBox(root,
                                         values=colours,
                                         font=("Arial", 20, "bold"),
                                         dropdown_font=("Arial", 20, "bold"),
                                         corner_radius=2,
                                         fg_color="white",
                                            button_hover_color="gray",
                                            dropdown_hover_color="gray",
                                         dropdown_text_color="black",
                                         border_color="black",
                                            border_width=2,
                                            button_color="black",
                                            dropdown_fg_color="white",
                                            text_color="black",
                                            hover=True, # can change it false so the hovering of the selector thing is not a different colour
                                            justify="center", # changes the placement of the text in the combobox, you can also use "left" or "right"
                                            state="normal" # you can change this to "disabled" and it will be greyed out and you can't click it, or to "readonly" and you can only select the options in the combobox, but you can't type in it
                                         ) # you can put the colour picker command here if you want it to change the label when you pick a colour, but i will show you how to do it with a button instead
my_combobox.pack(pady=10)

#create button to pick colour
my_button = customtkinter.CTkButton(root, text="Pick a colour!", command=colour_picker2)
my_button.pack(pady=10)

#create button for red colour
red_button = customtkinter.CTkButton(root, text="Red", command= colour_picker_red)
red_button.pack(pady=10)

#create output label
output_label = customtkinter.CTkLabel(root, text=" ")
output_label.pack(pady=20)

root.mainloop()