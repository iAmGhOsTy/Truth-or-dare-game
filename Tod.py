#importing modules and data
from tkinter import *
from truths import truth
from dares import dare
import random

#creating the gui   

#initializing the window
root = Tk()

#setting the title and background colour
root.configure(background = "darkBlue")
root.title("Truth or Dare")

#self defined functions
def getTruth():
    return random.choice(truth)

def getDare():
    return random.choice(dare)

def changeTruth():
    lable1.config(text=f"{getTruth()}")
    lable1.grid(row=1,column=1,columnspan=3)

def changeDare():
    lable1.config(text=f"{getDare()}")
    lable1.grid(row=1,column=1,columnspan=3)

#creating frames
#frame = Frame(root,height=100,width=400,background="darkBlue").pack()

#creating Lables

global lable1
lable1 = Label(root, text=f"{getTruth()}",bg="#abdbe3",font="Terminal",padx=10,pady=10)
lable1.grid(row=1,column=1,columnspan=3,padx=10,pady=10)

#creating the widgets

#Buttons, have .place() method,.grid() method and .pack() method

truthButton = Button(root, text = "Truth", command = changeTruth,width=10,font="Fixedsys").grid(column=1,row=3,padx=10,pady=10)
dareButton = Button(root, text = "Dare", command = changeDare,width=10,font="Fixedsys").grid(column=2,row=3,padx=10,pady=10)
quitButton = Button(root, text = "Quit", command = root.destroy,width=10,font="Fixedsys").grid(column=3,row=3,padx=10,pady=10)



#main loop
root.mainloop()