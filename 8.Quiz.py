from tkinter import tk
y= 0 #y starts @ 0
a = ttk.Notebook() #.notebook , dira more research
frame1 = ttk.Frame(a) # .()
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)


#open window
root = ttk.Frame(a)
root.title("Quiz")

def quiz(a):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")
    
    #1
    Label(frame1, text="Age when first put in Jail?", font=("Arial", 50, "bold")).grid()
    Button(frame1, text="20", font=("Arial", 30, "bold"), bg="light blue", command=a_right).grid(row=3, column=1)
    Button(frame1, text="26", font=("Arial", 30, "bold"),bg="light green", command=a_wrong).grid(row=3,column=2)
    Buttom(frame1, text="30", font=("arial", 30, "bold"), bg="light prink", command=a_wrong).grid(row=3,column=3)
    
   #2
     Label(frame2, text="Prisoner's Age?", font=("Arial", 50, "bold")).grid()
    Button(frame2, text="33", font=("Arial", 30, "bold"), bg="light blue", command=a_wrong2).grid(row=3, column=1)
    Button(frame2, text="31", font=("Arial", 30, "bold"), bg="light green", command=a_wrong2).grid(row=3, column=2)
    Button(frame2, text="30", font=("arial", 30, "bold"), bg="light pink", command=a_right2).grid(row=3, column=3)

    #3
    Label(frame3, text="Age they will be allowed to leave Prison?", font=("Arial", 50, "bold")).grid()
    Button(frame3, text="33", font=("Arial", 30, "bold"), bg="light blue", command=a_wrong2).grid(row=3, column=1)
    Button(frame3, text="31", font=("Arial", 30, "bold"), bg="light green", command=a_wrong2).grid(row=3, column=2)
    Button(frame3, text="30", font=("arial", 30, "bold"), bg="light pink", command=a_right2).grid(row=3, column=3)
    
    #4
    Label(frame4, text="Life expectancy?", font=("Arial", 50, "bold")).grid()
    Button(frame4, text="33", font=("Arial", 30, "bold"), bg="light blue", command=a_wrong2).grid(row=3, column=1)
    Button(frame4, text="31", font=("Arial", 30, "bold"), bg="light green", command=a_wrong2).grid(row=3, column=2)
    Button(frame4, text="30", font=("arial", 30, "bold"), bg="light pink", command=a_right2).grid(row=3, column=3)
    #5
    Label(frame5, text="Age in 2023?", font=("Arial", 50, "bold")).grid()
    Button(frame5, text="33", font=("Arial", 30, "bold"), bg="light blue", command=a_wrong2).grid(row=3, column=1)
    Button(frame5, text="31", font=("Arial", 30, "bold"), bg="light green", command=a_wrong2).grid(row=3, column=2)
    Button(frame5, text="30", font=("arial", 30, "bold"), bg="light pink", command=a_right2).grid(row=3, column=3)





  
 def a_right():
     Label(frame1,text="Correct",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame1,text="Marks Obtained : 1",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
     
def a_wrong():
     Label(frame1,text="Incorrect",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame1,text="Marks Obtained : 0",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
 
 def a_right2():
     Label(frame2,text="Correct",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame2,text="Marks Obtained : 1",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
     
def a_wrong2():
     Label(frame2,text="Incorrect",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame2,text="Marks Obtained : 0",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
 
 def a_right3():
     Label(frame3,text="Correct",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame3,text="Marks Obtained : 1",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
     
def a_wrong3():
     Label(frame3,text="Incorrect",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame3,text="Marks Obtained : 0",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
    
 def a_right4():
     Label(frame4,text="Correct",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame4,text="Marks Obtained : 1",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
     
def a_wrong4():
     Label(frame4,text="Incorrect",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame4,text="Marks Obtained : 0",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
 
 def a_right5():
     Label(frame1,text="Correct",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame1,text="Marks Obtained : 1",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
     
def a_wrong5():
     Label(frame1,text="Incorrect",font=("Arial", 40,"bold"),background="green",fg="yellow" ).grid(row=1,column=2)
     Label(frame1,text="Marks Obtained : 0",font=("Arial", 40,"bold"),background="black",fg="white" ).grid(row=1,column=3)
 

quiz(y)
a.pack()
a.mainloop()

root.mainloop()
