from tkinter import *
from typing import Container
#----------------------------------------------------------------
def Login_screen():
    Login = Tk()
    Login.title('Omakasa')

    LogIn_txt = Label(Login,text='Login',font=("Arial Bold", 25)).pack(pady=10)
    frame1= Frame().pack(pady=5)
    Id_in = StringVar()
    LogIn_user_txt = Label(master=frame1,text='Username',font=("Arial", 14)).pack()
    LogIn_user_box = Entry(master=frame1,textvariable=Id_in,width=28,font=("Arial",12)).pack(ipady=4,ipadx=8)

    frame2 = Frame().pack(pady=5)
    Pass_in = StringVar()
    LogIn_pass_txt = Label(master=frame2,text='Password',font=("Arial", 14)).pack()
    LogIn_pass_box = Entry(master=frame2,textvariable=Pass_in,show='*',width=28,font=("Arial",12)).pack(ipady=4,ipadx=8)

    def checkLogin():
        ID_INPUT = Id_in.get()
        PASS_INPUT = Pass_in.get()
        Login_file = open('Omakasa/Data/admin.txt', 'r')
        Id,Pass = Login_file.read().split('\n')
        if Id == ID_INPUT and Pass == PASS_INPUT:
            print('Log In succes!') 
            Login.destroy()
            main_screen()
        else : print('Log In failed!')
        Login_file.close()
    
    LogIn_btn = Button(Login,text='Log In',command=checkLogin,bg="white",width=7,height=1,bd=3,font=("Arial Bold", 10)).pack(pady=15)

    Login.geometry("450x300+500+200")
    Login.mainloop() 
    #----------------------------------------------------------------
def main_screen():
    root = Tk()
    root.title('Omakasa')


    LogIn_txt = Label(root,text='OMAKASA',font=("Arial Bold", 45)).place(x=10,y=3)
    Search_box  = Entry(root,font=("Arial", 18)).place(x=350,y=100)
    Search_button = Button(root,text='ค้นหา',font=("Arial Bold", 15)).place(x=620,y=95)

    Container_costomer = Frame(root,bg="white")
    label = Label(master=Container_costomer,text='ควย',font=("Arial", 18)).grid(column=0,row=0)
    label2 = Label(master=Container_costomer,text='ควย',font=("Arial", 18)).grid(column=1,row=0,padx=50)
    Container_costomer.place(width=650,height=500,x=35,y=175)
    root.geometry("720x720+300+0")
    root.mainloop() 
    
Login_screen()