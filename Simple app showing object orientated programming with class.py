from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #root = customtkinter.CTk()

        #text box
        self.my_text = customtkinter.CTkTextbox(self, width=600, height=300)
        self.my_text.pack(pady=20)

        self.my_button = customtkinter.CTkButton(self, text="Clear Box", command=self.clear)
        self.my_button.apck(pady=20)
    def clear(self):
        self.my_text.delete(0.0, END) #you can put this anywhere now, but you have to keep it in the class


#Create app's main loop after defining it
app = App()
App.mainloop()