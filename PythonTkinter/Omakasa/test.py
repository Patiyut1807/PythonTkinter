#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x350")

#Define a function to submit the validate the value of Entry widget
def submit_name():
   Label(frame, text="Hello "+ entry.get(), font=('Helvetica',12, 'bold')).pack(pady=20)
   submit.configure(state= "disabled")

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=3)
frame.pack()
#Create an Entry widget in the Frame for Accepting the Username
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Name")
entry.pack(ipadx= 30, ipady=30)

#Set the focus on Entry1
entry.focus_set()

#Create a submit button
submit= ttk.Button(win, text= "submit",command=submit_name)
submit.pack(pady=10)
win.mainloop()