import tkinter
from tkinter import *

root = Tk() //root.Tk() to this
root.title("To-Do-List")
root.geometry("300x700+200+200")//root.geometry("300x700x200") to this
root.resizable(False,False)

task_list= []

def addTask():
   task = task_entry.get()
   task_entry.delete(0, END)
   
   if task:
      with open("tasklist.tt", 'a') as taskfile:
           taskfile.write(f"\n{task}")
      task_list.append(task)
      listbox.insert(  END, task)
      
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
    task_list.remove(task)
    with open("tasklis.txt",'w') as taskfile:
         for task in task_list:
              taskfile.write(task+"\n")
              
    listbo.delete( ANCHOR )          
   
def openTaskFile():

   try:
    global task_list
    with open("tasklist.txt","r") as taskfile:
         tasks = taskfile.readline()
         
    for task in tasks:
        if task != '\n\:
            task_list.append(task)
            listbox.insert(END, task)
            
    except:
    file = open("tasklist.txt', 'w')
    file.close()
    


#icon
Image_icon=PhotoImage()#linktopic
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage()#linktopic
Label(root,image=TopImage).pack()

dockImage=PhotoImage()#linkofimage
Label(root,image=dockImage,bg="pink").place(x=30,y=25

noteImage=PhotoImage()#img link
Label(root,image=noteImage,bg="blue").place(x=30,y=25)

heading=Label(root,text="ALL TASk", font="arial 20 bold",fg="white",bg="gray")
heading.pace(x=130,y=20)

#main
frame= Frame(root, width= 400,height=50,bg="white")
frame.place(x=0,y=189)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="green,fg="#fff",bd=0,command=addTask)
button.place=300,y=0)

#listbox
frame1 = Frame(root,bd=3,width=700,height=280,bg="red")
frame1.pack(pady=(160,0))

lstbox=Listbox(frame1,font=('arial',122),width=40,height=16,bg="black",fg="white",cursor="hand2")
listbox.pack(side=LEFT, fill= BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete
Delete_icon=PhotoImage()#linktoimg
Button(root,image=Delete_icon,bd=0).pack()




root.mainloop()

