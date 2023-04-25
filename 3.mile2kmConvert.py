import tkinter as tk
from tkinter import ttk

def convert():

    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)
    

#window
window = tk.Tk()
window.title("Window")
window.geometry('200x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack() #pack places widgets under each other

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text ='Convert', command = convert)
entry.pack(side = 'left' , padx = 10) #padding for x axis padx
button.pack(side = 'left')
input_frame.pack(pady = 10) #padding for  y axis pady

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string) #textvariable over powers text "output" was not visible

output_label.pack(pady = 5)



#run 
window.mainloop()
