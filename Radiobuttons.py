from tkinter import *
import customtkinter

root = customtkinter.CTk()

my_label2 = customtkinter.CTkLabel(root, text="", font=("Arial", 20))
my_label2.pack(pady=50)

def get_rad():
    if radio_var.get() == "yes":
        my_label2.configure(text="You like pizza!")
    elif radio_var.get() == "no":
        my_label2.configure(text="You don't like pizza!")
    else:
        my_label2.configure(text="You didn't select an option.")

my_label = customtkinter.CTkLabel(root, text="Do you like pizza?", font=("Arial", 20))
my_label.pack(pady=20)

#assigning it a neutral value so that it doesn't default to the first option
radio_var = customtkinter.StringVar(value="other") #int for numbers

my_rad1 = customtkinter.CTkRadioButton(root, text="Yes I do", value="yes", variable=radio_var,
                                        width=200,  # Set the width of the radio button
                                        height=40,  # Set the height of the radio button
                                        corner_radius=20,  # Set the corner radius for rounded edges
                                        fg_color="black",  # Set the foreground color (text color)
                                        hover_color="lightgreen",  # Set the hover color
                                        text_color="purple"  # Set the text color
                                       )
my_rad1.pack(pady=10)

my_rad2 = customtkinter.CTkRadioButton(root, text="No I don't", value="no", variable=radio_var,
                                        width=200,  # Set the width of the radio button
                                        height=40,  # Set the height of the radio button
                                        corner_radius=20,  # Set the corner radius for rounded edges
                                        fg_color="black",  # Set the foreground color (text color)
                                        hover_color="lightcoral",  # Set the hover color
                                        text_color="purple"  # Set the text color
                                       )
my_rad2.pack(pady=10)

my_button = customtkinter.CTkButton(root, text="Submit", command=get_rad)
my_button.pack(pady=20)

root.mainloop()