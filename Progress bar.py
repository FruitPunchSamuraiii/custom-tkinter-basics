from tkinter import *
import customtkinter

root = customtkinter.CTk()

def clicker():
    my_progressbar.step()
    my_label.configure(text=f"{int(my_progressbar.get() * 100)}%")

def update_label():
    # Convert progress (0.0 to 1.0) into a percentage
    progress_pct = int(my_progressbar.get() * 100)
    my_label.configure(text=f"{progress_pct}%")
    
    # Keep updating every 50ms while the loop is running
    root.after(50, update_label)

def start():
    my_progressbar.start()
    update_label()  # Start updating the label when the progress bar starts

def stop():
    my_progressbar.stop()

my_progressbar = customtkinter.CTkProgressBar(root, 
                                              width=400, 
                                              orientation="horizontal",
                                              mode="determinate", # mode where it goes to end and starts again at 0, indeterminante it starts going down again rather than jumping to 0
                                              determinate_speed=5, # speed of the progress bar when in determinate mode
                                                indeterminate_speed=0.01, # speed of the progress bar when in indeterminate mode
                                                height=20, # height of the progress bar
                                                corner_radius=40, # corner radius of the progress bar
                                                progress_color="blue", # colour of the progress bar
                                                border_color="black", # colour of the border of the progress bar
                                                border_width=2, # width of the border of the progress bar
                                                bg_color="white" # background colour of the progress bar
                                              )
my_progressbar.pack(pady=40)

#set the default progress
my_progressbar.set(0) # 1 is 100% and 0 is 0%

my_button = customtkinter.CTkButton(root, text="Click me", command=clicker)
my_button.pack(pady=10)

start_button = customtkinter.CTkButton(root, text="Start", command=start)
start_button.pack(pady=10)

stop_button = customtkinter.CTkButton(root, text="Stop", command=stop)
stop_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

root.mainloop()