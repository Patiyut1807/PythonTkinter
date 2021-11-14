from tkinter import *

def Login_screen():
    Login = Tk()
    Login.title('Omakasa')
    Login['background']='#FFF'
    LogIn_txt = Label(Login,text='Login',font=("Arial Bold", 25),background="#FD650D",fg='white').pack(pady=10,fill=X)
    frame1= Frame().pack(pady=5)
    Id_in = StringVar()
    LogIn_user_txt = Label(frame1
                           ,text='Username'
                           ,font=("Arial", 14)
                           ,bg='white').pack()
    LogIn_user_box = Entry(frame1
                           ,textvariable=Id_in
                           ,width=28
                           ,font=("Arial",12)
                           ,bd='2').pack(ipady=4,ipadx=8)

    frame2 = Frame().pack(pady=5)
    Pass_in = StringVar()
    LogIn_pass_txt = Label(frame2,text='Password',font=("Arial", 14),bg='white').pack()
    LogIn_pass_box = Entry(frame2,textvariable=Pass_in,show='*',width=28,font=("Arial",12),bd='2').pack(ipady=4,ipadx=8)
   
    
    def checkLogin():
        ID_check = FALSE
        ID_INPUT = Id_in.get()
        PASS_INPUT = Pass_in.get()
        Login_file = open('Omakasa/Data/admin.txt', 'r')
        Id = Login_file.read().split('\n')
        for ID in Id :
            if ID == ID_INPUT and 'omakasa6401'== PASS_INPUT:
                ID_check = TRUE
        if ID_check :
            Login.destroy()
            main_screen()
        else : 
            Hint_error_text.config(fg='red')
        Login_file.close()
    Hint_error_text = Label(Login,text='Your username or password is incorrect',bg='white',fg='white')
    Hint_error_text.pack()
    LogIn_btn = Button(Login
                       ,text='Log In'
                       ,command=checkLogin
                       ,width=7,height=1
                       ,bd=3
                       ,font=("Arial Bold", 10)
                       ,background="#FD650D"
                       ,fg='white'
                       ,relief=FLAT)
    LogIn_btn.pack(pady=15)
    Login.geometry("450x300+500+200")
    Login.mainloop() 
    
Login_screen()