from tkinter import *
import customtkinter

root = customtkinter.CTk()

#create a scrollable frame
my_frame = customtkinter.CTkScrollableFrame(root, 
                                            orientation="vertical",
                                            width=300,
                                            height=200,
                                            label_text="Hello World!",
                                            label_fg_color="MediumPurple3",
                                            label_text_color="Black",
                                            label_font=("Arial", 20),
                                            label_anchor="center", # where the text is positioned using compass points
                                            border_width=3,
                                            border_color="Pink",
                                            fg_color="orange",
                                            scrollbar_fg_color="Black",
                                            scrollbar_button_color="Blue",
                                            scrollbar_button_hover_color="Red",
                                            corner_radius=4
                                            )
my_frame.pack(pady=40)

#for loop for buttons
for x in range(20):
    my_button = customtkinter.CTkButton(my_frame, text=f"Button {x}")
    my_button.pack(pady=10)

root.mainloop()