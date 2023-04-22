from tkinter import *
import random

window = Tk()
window.title('KamoK')
window.geometry('700x500')

Label(window, font=('bold', 10), text='PASSWORD GENERATOR').pack()

len1 = IntVar()
len2 = IntVar()
len3 = IntVar()

def password_generate(leng):
    valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'
    password = ''.join(random.sample(valid_char, leng))
    password_label.config(text=password)

password_label = Label(window, font=('bold', 20))
password_label.place(x=190, y=50)

generate_button = Button(window, text='Generate Password', font=('bold', 12), command=get_len)
generate_button.place(x=190, y=150)

Checkbutton(text='4 character', onvalue=4, offvalue=0, variable=len1).place(x=200, y=200)
Checkbutton(text='6 character', onvalue=6, offvalue=0, variable=len2).place(x=200, y=220)
Checkbutton(text='8 character', onvalue=8, offvalue=0, variable=len3).place(x=200, y=240)

# function to check the checkbox
def get_len():
    if len1.get() == 4:
        password_generate(4)
    elif len2.get() == 6:
        password_generate(6)
    elif len3.get() == 8:
        password_generate(8)
    else:
        password_generate(6)

Button(window, text='Generate', font=('normal', 10), bg='black', fg='white', command=get_len).place(x=200, y=100)

window.mainloop()
