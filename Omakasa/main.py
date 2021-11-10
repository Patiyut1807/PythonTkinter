from tkinter import *
root = Tk()
root.title('Omakasa')

username = StringVar()
password = StringVar()

LogIn_txt = Label(root,text='Login',font=("Arial Bold", 25)).grid(column=1,row=0)
LogIn_user_txt = Label(root,text='Username',font=("Arial", 15)).grid(column=2,row=1)
LogIn_pass_txt = Label(root,text='Password',font=("Arial", 15)).grid(column=2,row=3)

LogIn_user_box = Entry(root,textvariable=username).grid(column=2,row=2)
LogIn_pass_box = Entry(root,textvariable=password).grid(column=2,row=4)


LogIn_btn = Button(root,text='Log In').grid(column=2,row=5)



    
root.geometry("720x720+300+0")
root.mainloop() 
