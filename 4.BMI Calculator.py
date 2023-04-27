from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# pip install pillow -> comment out because it's not necessary here

root = Tk()
root.title("BMI Calculator")
root.geometry("500x700")  # removed the invalid 'x900'
root.configure(bg="orange")

def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # convert height into meter
    m = h / 100
    bmi = round(float(w / m ** 2))
    label1.config(text=bmi)

    # fix the syntax errors in these if-elif statements
    if bmi <= 18.5:
        label2.config(text="Underweight")
        label3.config(text="You have lower weight than normal body!")
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal")
        label3.config(text="")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight")
        label3.config(text="It indicates that a person is slightly overweight!")
    else:
        label2.config(text="Obese!")
        label3.config(text="You have higher weight than average body! A doctor may advise to lose some weight for health")

# comment out the undefined functions, photo_picture and icon_picture, and the missing link
# also fix the typo "tet" -> "text" in label3 of the BMI function

# icon
icon_pic = None  # replace None with the actual link to the icon img
root.iconphoto(False, ImageTk.PhotoImage(Image.open(icon_pic)))

# top
top_pic = None  # replace None with the actual link to the top img
top_picture = Label(root, image=ImageTk.PhotoImage(Image.open(top_pic)), bg="blue")
top_picture.pack(side=TOP)

# bottom box
Label(root, width=72, height=18, bg="light blue").pack(side=BOTTOM)

# two boxes
box_pic = None  # replace None with the actual link to the box img
Label(root, image=ImageTk.PhotoImage(Image.open(box_pic))).place(x=20, y=100)
Label(root, image=ImageTk.PhotoImage(Image.open(box_pic))).place(x=240, y=100)
#############Slider 1#####################
# scale 1
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = Image.open("")  # replace "" with the actual link to the scale img
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2

current_value = tk.DoubleVar()
scale = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
scale.place(x=80, y=310)  # adjust the y coordinate to avoid overlapping with the bottom box




##########################################


#@@@@@@@@@@@@Slider 2@@@@@@@@@@@@@@@@@@@@@
# Scale 2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Height.set(get_current_value2())

# Command to change BG Color of scale
style2 = ttk.Style()
style2.configure("TScale", background="gray")

slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Entry box
Height = StringVar()
Height = StringVar()
Height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER) #to align text in 
Height.set(get_current_value2())

weight=Entry(root,textvarriable=weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER) #to align text in
weight.place(x=255,y=160)
Weight.set(get_current_value2())

#man image
secondimage = Label(root,bg="lightblue")
secondimage.place(x=70,y=530)

Button(root,tet = "View Report", width= 15, height=2,font="arial 10 bold",bg="#1f6e68",fg="white").place(x=280,y=340)


label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=305)

label2=Label(root,font="arial 60 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=280,y=450)

label3=Label(root,font="arial 60 bold",bg="lightblue")
label3.place(x=200,y=500)


root.mainloop()
