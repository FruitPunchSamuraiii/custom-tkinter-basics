import customtkinter
from tkinter import END

# Set the theme and colour options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# 1. Create the main window FIRST
root = customtkinter.CTk()

# 2. Initialize the StringVar AFTER creating root
check_var = customtkinter.StringVar(value="off")
#checkbox text
text_var = customtkinter.StringVar(value="Click Me")

def game():
    if check_var.get() == "on": #checks if the checkbox is checked
        my_label.configure(text="You Clicked it") #changes what it says
    else:
        my_label.configure(text="You didn't click it") #changes what it says

    text_var.set("You clicked the button") #changes the text of the button

def clear():
    my_check.deselect() #deselects the checkbox
    my_label.configure(text=" ") #clears the label text
    text_var.set("Click Me") #changes the text of the button back to the original text

my_check = customtkinter.CTkCheckBox(
    root,
    text="Would you like to play a game?",
    variable=check_var,
    onvalue="on",
    offvalue="off",
    checkbox_width=20,
    checkbox_height=20,
    font=("Arial", 20, "bold"),
    corner_radius=2,
    fg_color="white", #changes the colour of the checkbox when it is checked
    hover_color="gray", #changes the colour of the checkbox when it is hovered over
    hover=True, # if you chang ethis to false, hovering it doesn't change the colour of the checkbox
    textvariable=text_var
)
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Click Me", command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)

toggle_button = customtkinter.CTkButton(root, text="Toggle", command=my_check.toggle) #toggles the checkbox on and off
toggle_button.pack(pady=10)

select_button = customtkinter.CTkButton(root, text="Select", command=my_check.select) #selects the checkbox without letting the user deselect it
select_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text=" ")
my_label.pack(pady=20)

root.mainloop()