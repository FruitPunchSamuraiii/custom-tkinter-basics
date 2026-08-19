import customtkinter
from tkinter import END

#Set the theme and colour options

customtkinter.set_appearance_mode("dark") #Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue") #Themes: "blue" (standard), "dark-blue", "green", "orange"

#root = Tk() Create a Tk window like you normally do

root = customtkinter.CTk() #Create a CTk window like you do with the Tk window

# different functions for the labels and buttons

def hello():
    my_label.configure(text=my_button.cget("text")) #returns text of button and sets it to label

def submit():
    my_label2.configure(text=f'hello {my_entry.get()}') #returns text of entry and sets it to label
    my_entry.configure(state="disabled") #disables entry box after submit button is pressed

def clear():
    my_entry.delete(0, END) #which positions in the box by index get deleted
    my_entry.configure(state="normal")

#buttons

my_button = customtkinter.CTkButton(root,
   text="Submit",
   command=submit,
   height=40,
   width=200,
   font=("Arial", 20),
   text_color="white",
   fg_color="blue",
   hover_color="green",
   corner_radius=10,
   bg_color="black",
   border_color="red",
   border_width=2,
   state="normal"
   ) 

my_button.pack(pady=20, padx=60)

my_entry = customtkinter.CTkEntry(root, placeholder_text="Enter text here",
 width=200,
   height=40, 
   border_width=2, 
   corner_radius=10,
   placeholder_text_color="blue")

my_entry.pack(pady=20, padx=60)

clear_button = customtkinter.CTkButton(root, text='Clear', command=clear)
clear_button.pack(pady=20, padx=60) #where on screen it is

#labels

my_label2 = customtkinter.CTkLabel(root, text=" ")
my_label2.pack(pady=20, padx=60)

my_label = customtkinter.CTkLabel(root, text=" ")
my_label.pack(pady=20, padx=60)

root.mainloop()