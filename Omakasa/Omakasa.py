from tkinter import *
# ----------------------------------------------------------------


def Login_screen():
    Login = Tk()
    Login.title('Omakasa')
    Login['background'] = '#FFF'
    LogIn_txt = Label(Login, text='Login', font=(
        "Arial Bold", 25), background="#FD650D", fg='white').pack(pady=10, fill=X)
    frame1 = Frame().pack(pady=5)
    Id_in = StringVar()
    LogIn_user_txt = Label(frame1, text='Username',
                           font=("Arial", 14), bg='white').pack()
    LogIn_user_box = Entry(frame1, textvariable=Id_in, width=28, font=(
        "Arial", 12), bd='2').pack(ipady=4, ipadx=8)

    frame2 = Frame().pack(pady=5)
    Pass_in = StringVar()
    LogIn_pass_txt = Label(frame2, text='Password',
                           font=("Arial", 14), bg='white').pack()
    LogIn_pass_box = Entry(frame2, textvariable=Pass_in, show='*',
                           width=28, font=("Arial", 12), bd='2').pack(ipady=4, ipadx=8)

    def checkLogin():
        ID_check = FALSE
        ID_INPUT = Id_in.get()
        PASS_INPUT = Pass_in.get()
        Login_file = open('Omakasa/Data/admin.txt', 'r')
        Id = Login_file.read().split('\n')
        for ID in Id:
            if ID == ID_INPUT and 'omakasa6401' == PASS_INPUT :
                ID_check = TRUE
        if ID_check:
            Login.destroy()
            main_screen()
        else:
            Hint_error_text.config(fg='red')
        Login_file.close()
    Hint_error_text = Label(
        Login, text='Your username or password is incorrect', bg='white', fg='white')
    Hint_error_text.pack()
    LogIn_btn = Button(Login, text='Log In', command=checkLogin, width=7, height=1, bd=3, font=(
        "Arial Bold", 10), background="#FD650D", fg='white', relief=FLAT)
    LogIn_btn.pack(pady=15)
    Login.geometry("450x300+500+200")
    Login.mainloop()

    # ----------------------------------------------------------------
n = 0


def main_screen():
    root = Tk()
    root.title('Omakasa')

    def add_row():
        global n
        frm_row = Frame(frm_table, width=650, height=15, pady=1, bg="#a8a5a5")
        frm_row.pack()
        table_n = Label(frm_row, text=n, font=("Arial", 13), width=2)
        customer = Label(frm_row, text='Patipan', font=(
            "Arial", 13), width=15, bg='white')
        customer_n = Label(frm_row, text='5', font=("Arial", 13), width=3)
        checkIn = Label(frm_row, text='11/11/64 -11:11',
                        font=("Arial", 13), width=15, bg='white')
        checkOut = Label(frm_row, text='11/11/64 -12:11',
                         font=("Arial", 13), width=15)
        lb_price = Label(frm_row, text='500', font=(
            "Arial", 13), padx='25', width=4, bg='white')
        btn_bill = Button(frm_row, text='เช็คบิล', padx=15,
                          height=1, background="#49FF00")

        table_n.grid(column=0, row=0)
        customer.grid(column=1, row=0)
        customer_n.grid(column=2, row=0)
        checkIn.grid(column=3, row=0)
        checkOut.grid(column=4, row=0)
        lb_price.grid(column=5, row=0)
        btn_bill.grid(column=6, row=0)
        n += 1
    LogIn_txt = Label(root, text='OMAKASA', font=(
        "Arial Bold", 45), background="#FD650D", fg='white').place(x=10, y=10)
    Search_box = Entry(root, font=("Arial", 16), width=20).place(x=370, y=90)

    Search_button = Button(root, text='ค้นหา', font=(
        "Arial Bold", 13), background="#FD650D", fg='white', command=add_row).place(x=620, y=87)

    frm_table = Frame(root, bg="white")
    frm_table.place(width=650, height=500, x=35, y=175)

    scr_bar = Scrollbar(frm_table)
    scr_bar.pack(side=RIGHT, fill=Y)
    root.geometry("720x720+300+0")
    root.mainloop()


Login_screen()
