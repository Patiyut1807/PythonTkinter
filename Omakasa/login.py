from tkinter import *
Login = Tk()
Login.title('Omakasa')
wrap_box = Label(Login,text='                 ',font=("Arial Bold", 25)).grid(column=1,row=0)

LogIn_txt = Label(Login,text='Login',font=("Arial Bold", 25)).grid(column=2,row=1)
LogIn_user_txt = Label(Login,text='Username',font=("Arial", 15)).grid(column=2,row=2)
LogIn_pass_txt = Label(Login,text='Password',font=("Arial", 15)).grid(column=2,row=4)

Id_in = StringVar()
LogIn_user_box = Entry(Login,textvariable=Id_in).grid(column=2,row=3)
Pass_in = StringVar()
LogIn_pass_box = Entry(Login,textvariable=Pass_in).grid(column=2,row=5)

wrap_box = Label(Login,text='                 ',font=("Arial Bold", 25)).grid(column=1,row=6)


def checkLogin():
    ID_INPUT = Id_in.get()
    PASS_INPUT = Pass_in.get()
    Login_file = open('Omakasa/Data/admin.txt', 'r')
    Id,Pass = Login_file.read().split('\n')
    if Id == ID_INPUT and Pass == PASS_INPUT:
            print('Log In succes!') 
            
    else : print('Log In failed!')
    Login_file.close()
    
LogIn_btn = Button(Login,text='Log In',command=checkLogin).grid(column=2,row=7)


Login.geometry("450x300+500+200")
Login.mainloop() 