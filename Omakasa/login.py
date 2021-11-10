from tkinter import *
Login = Tk()
Login.title('Omakasa')

username = StringVar()
password = StringVar()
wrap_box = Label(Login,text='                 ',font=("Arial Bold", 25)).grid(column=1,row=0)
LogIn_txt = Label(Login,text='Login',font=("Arial Bold", 25)).grid(column=2,row=1)
LogIn_user_txt = Label(Login,text='Username',font=("Arial", 15)).grid(column=2,row=2)
LogIn_pass_txt = Label(Login,text='Password',font=("Arial", 15)).grid(column=2,row=4)

LogIn_user_box = Entry(Login,textvariable=username).grid(column=2,row=3)
LogIn_pass_box = Entry(Login,textvariable=password).grid(column=2,row=5)

wrap_box = Label(Login,text='                 ',font=("Arial Bold", 25)).grid(column=1,row=6)
LogIn_btn = Button(Login,text='Log In').grid(column=2,row=7)



    
Login.geometry("450x300+500+100")
Login.mainloop() 