from tkinter import Tk
from tkinter import Label
import time 

root = Tk()
root.title("Digital Clock-K")

def present_time():
    display_time = time.strftime("%I:%M:%S: %p")
    clock.config(text=display_time)
    clock.after(200, present_time) #after 200milisec present time function will run

clock = Label(root, font=("arial", 130), bg="blue", fg="black") #fg is font color
clock.pack()

present_time()

root.mainloop()
