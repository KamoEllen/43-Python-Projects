#pip install pillow
#BodyMassIndex , given by mass(kg) & height(m) [kg % m^2]
#get images or use links


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("500x700x900")
root.configure(bg=orange)

def BMI():
    h=float(Height.get())
    w=float(Weight.get())
   
   #convert height into meter
   m=h/100
   bmi=round(float(w/m**2))
   #print(bmi)
   label1.config(text=bmi)
   
   #bmi of sa
   if bmi < = 18.5
   label2.config(text="Underweight")
   label3.config(tet="You have lower weight then nomal body!")
   
   elif bmi > 18.5 and bmi <= 25;
   label2.config(text="Normal")
   label3.config(tet="!")
   
   elif bmi > 25 and bmi <= 30;
   label2.config(text="Overweight")
   label3.config(tet="It indicates that a person is \n slightly overweight \n!")
   
   else:
   label2.config(text="Obese!")
   label3.config(tet="You have higher weighht than average body! \n A doctor may advise to lose some \n weight for health")
   
   
   
   
#icon , get link
icon_pic = photo_picture() #link to icon img
root.picture(False,icon_pic)

#top
top=icon_picture() #link
top_picture=Label(root,image=top,background=blue)
top_picture.pack(x =-1, y =-1)

#bottom box
Label(root,width = 72, height = 18, bg ="light blue").pack(side = BOTTOM)

#two boxes
box = photo_picture()#boximg
Label(root,image=box).place(x=20, y = 100)
Label(root,image=box).place(x=240, y= 100)

#scale
scale=photo_picture() #scale img ink
Label(root,image=scale,bg="lightpink").place(x=20,y=310)

#############Slider 1#####################
curent_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img = (Image.open(" "))
    resized_image=img.esize((50,10+size))
    photo2=ImageTk.photo_picture(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2
   
#COMMAND to change BG Color of scale

style = ttk.Style()
style.configure("TScale",background="gray")
slider.ttk.Scale(root,from_=0,to = 220, orient = 'horizontal', style ="TScale", command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

##########################################


#@@@@@@@@@@@@Slider 2@@@@@@@@@@@@@@@@@@@@@

curent_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Height.set(get_current_value2())

   
#COMMAND to change BG Color of scale

style2 = ttk.Style()
style2.configure("TScale",background="gray")
slider2=ttk.Scale(root,from_=0,to = 200, orient = 'horizontal', style ="TScale", command=slider_changed2 ,variable=current_value2)
slider2.place(x=300,y=250)

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
