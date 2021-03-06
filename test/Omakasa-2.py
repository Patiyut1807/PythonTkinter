from tkinter import *
from tkinter import ttk
import time
# -------------------------------------------------------------------
admin = ""
DATA = []
count = 0
data_search = []
INDEX =''
# -----def function---------------------------------------------------

def pull_index():
    global INDEX
    f = open(f'Omakasa/Data/index.txt','r')
    INDEX = int(f.read())
    f.close()
# ---------------tkinterUI--------------------------------------
def Login_screen():
    Login = Tk()
    Login.title('Omakasa')
    Login['background'] = '#FFF'
    LogIn_txt = Label(Login, text='Login', font=(
        "Arial Bold", 25), background="#FD650D", fg='white').pack(pady=10, fill=X)

    frame1 = Frame(Login).pack(pady=5)
    Id_in = StringVar()
    LogIn_user_txt = Label(frame1, text='Username',
                           font=("Arial", 14), bg='white').pack()
    LogIn_user_box = Entry(frame1, textvariable=Id_in, width=28, font=(
        "Arial", 12), bd='2').pack(ipady=4, ipadx=8)

    frame2 = Frame(Login).pack(pady=5)
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
        Login_file.close()
        for ID in Id:
            if ID == ID_INPUT and 'omakasa6401' == PASS_INPUT:
                ID_check = TRUE
                global admin
                admin = ID_INPUT
        if ID_check:
            Login.destroy()
            main_screen()
        else:
            Hint_error_text.config(fg='red')
    Hint_error_text = Label(
        Login, text='Your username or password is incorrect', bg='white', fg='white')
    Hint_error_text.pack()
    LogIn_btn = Button(Login, text='Log In', command=checkLogin, width=7, height=1, bd=3, font=(
        "Arial Bold", 10), background="#FD650D", fg='white', relief=FLAT)
    LogIn_btn.pack(pady=15)
    Login.geometry("450x300+500+200")
    Login.mainloop()

def main_screen():
    main = Tk()
    main.title('Omakasa')
    main.geometry("720x600+400+30")
    
    def add_screen():
        add = Tk()
        add.title('Omakasa-insert')
        add.geometry("200x160+600+250")
        add['bg'] = '#FD650D'

        frm_contain = Frame(add, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)
        lb = Label(add, text='?????????????????????????????????', fg='#FD650D',
                   bg='white', font=("Arial bold", 14)).pack()

        frm_name = Frame(frm_contain, bg='#FD650D', pady=10)
        lb_name = Label(frm_name, text='Name', bg='white')
        en_name = Entry(frm_name, text='', width=13, font=("Arial", 14))
        frm_name.pack()
        lb_name.grid(column=0, row=0)
        en_name.grid(column=1, row=0)

        frm_amount = Frame(frm_contain, bg='#FD650D', pady=10)
        lb_amount = Label(frm_amount, text='Amount', bg='white')
        en_amount = Entry(frm_amount, text='', width=12, font=("Arial", 14))
        frm_amount.pack()
        lb_amount.grid(column=0, row=0)
        en_amount.grid(column=1, row=0)

        def add_data():
            if en_amount.get().isdigit():
                global admin
                global count
                global  INDEX
                time_w = time.time()
                time_format = time.localtime(time_w)
                DATA.append(
                    list((admin, en_name.get(), int(en_amount.get()), time_w, 0, 0, 0,INDEX)))
                tv_table.insert(parent='', index='end', iid=count, text='', values=(en_name.get(
                ), en_amount.get(), f'{time_format.tm_mday}/{time_format.tm_mon}/{time_format.tm_year}-{time_format.tm_hour}:{time_format.tm_min}', '-', '-', '-'))
                count += 1
                add.destroy()

        btn_add_data = Button(add, text='???????????????', bg='white',
                              relief=FLAT, width=10, height=1, command=add_data)
        btn_add_data.place(x=65, y=120)

        add.mainloop()

    def remove_screen():
        if not len(tv_table.selection()):
            return
        selected = tv_table.selection()[0]

        def del_data():
            DATA[int(selected)] = ['', '']
            tv_table.delete(selected)
            delete_promt.destroy()

        delete_promt = Tk()
        delete_promt.title('Omakasa-Delete')
        delete_promt.geometry("200x160+600+300")
        delete_promt['bg'] = 'white'

        lb_ask = Label(delete_promt, text='??????????????????????????????\n???????????????????????????????????????????????????????',
                       bg='white', font=("Arial", 13), pady=15)
        btn_confirm = Button(delete_promt, text='????????????',
                             command=del_data, width=7, height=2)
        btn_cancel = Button(delete_promt, text='??????????????????',
                            width=7, height=2, command=delete_promt.destroy)

        lb_ask.pack(pady=10)
        btn_confirm.pack(side=LEFT, padx=20)
        btn_cancel.pack(side=RIGHT, padx=20)
#----------------------?????????2-----entry-------------------------
    def edit_screen():
        if not len(tv_table.selection()):
            return
        edit = Tk()
        edit.title('Omakasa-edit')
        edit.geometry("200x200+600+150")
        edit['bg'] = '#FD650D'
        frm_contain = Frame(edit, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)
        lb = Label(edit, text='?????????????????????????????????', fg='#FD650D',
                   bg='white', font=("Arial bold", 14)).pack()

        frm_name = Frame(frm_contain, bg='#FD650D', pady=6)
        lb_name = Label(frm_name, text='Name', bg='white')
        en_name = Entry(frm_name, text='', width=13, font=("Arial", 14))
        frm_name.pack()
        lb_name.grid(column=0, row=0)
        en_name.grid(column=1, row=0)

        frm_amount = Frame(frm_contain, bg='#FD650D', pady=6)
        lb_amount = Label(frm_amount, text='Amount', bg='white')
        en_amount = Entry(frm_amount, text='', width=12, font=("Arial", 14))
        frm_amount.pack()
        lb_amount.grid(column=0, row=0)
        en_amount.grid(column=1, row=0)

        frm_date = Frame(frm_contain, bg='#FD650D', pady=10, padx=3)
        lb_day = Label(frm_date, text='??????????????????', bg='white', padx=1)
        en_day = Entry(frm_date, text='', width=2, font=("Arial", 12))
        lb_mon = Label(frm_date, text='???????????????', bg='white', padx=1)
        en_mon = Entry(frm_date, text='', width=2, font=("Arial", 12))
        lb_year = Label(frm_date, text='??????', bg='white', padx=1)
        en_year = Entry(frm_date, text='', width=2, font=("Arial", 12))

        box = Label(frm_date, text='', bg='#FD650D', padx=1, pady=10)
        lb_hour = Label(frm_date, text='?????????????????????', bg='white', padx=1)
        en_hour = Entry(frm_date, text='', width=2, font=("Arial", 12))
        lb_min = Label(frm_date, text='????????????', bg='white', padx=1)
        en_min = Entry(frm_date, text='', width=2, font=("Arial", 12))

        frm_date.pack()
        lb_day.grid(column=0, row=0)
        en_day.grid(column=1, row=0)
        lb_mon.grid(column=2, row=0)
        en_mon.grid(column=3, row=0)
        lb_year.grid(column=4, row=0)
        en_year.grid(column=5, row=0)
        lb_hour.grid(column=1, row=1)
        en_hour.grid(column=2, row=1)
        lb_min.grid(column=3, row=1)
        en_min.grid(column=4, row=1)
        box.grid(column=5, row=1)
#??????????????? edit_data
        def edit_data():
            select_item = int(tv_table.selection()[0])
            time_format = time.localtime(DATA[select_item][3])
            if en_name.get() != '':
                changed_name = en_name.get()
                DATA[select_item][1] = changed_name
            if en_amount.get() != '':
                changed_amount = en_amount.get()
                DATA[select_item][2] = int(changed_amount)
            time_edit = time.localtime(time.time())
            time_edit = list((time_edit.tm_year, time_edit.tm_mon, time_edit.tm_mday, time_edit.tm_hour,time_edit.tm_min, time_edit.tm_sec, time_edit.tm_wday, time_edit.tm_yday, time_edit.tm_isdst))
            check_edit = 0
            
            if en_day.get() != '' and int(en_day.get()) <= 31 and int(en_day.get()) > 0 :
                if int(en_day.get()) <= time_format.tm_mday and en_mon.get()=='' :
                    time_edit[1] =  time_edit[1]+1
                time_edit[2] = int(en_day.get())
                check_edit = 1    
            if en_mon.get() != '' and int(en_mon.get()) <= 12 and int(en_mon.get()) > 0 :
                if int(en_mon.get())<=time_format.tm_mon and en_year.get() =='':
                    time_edit[0] = time_edit[0]+1
                time_edit[1] = int(en_mon.get())
                check_edit = 1        
            
            if en_year.get() != '' and int(en_year.get()) <= 9999 and int(en_year.get()) > 0 and int(en_year.get())>=time_format.tm_year:
                time_edit[0] = int(en_year.get())
                check_edit = 1
                
            if en_hour.get() != '' and int(en_hour.get()) <= 23 and int(en_hour.get()) >= 0 :
                if int(en_hour.get())>time_format.tm_hour or (int(en_hour.get())<=time_format.tm_hour and en_day.get() !=''):
                    time_edit[3] = int(en_hour.get())
                    check_edit = 1
                elif int(en_hour.get())<=time_format.tm_hour and en_day.get() =='\0':
                    time_edit[3] = int(en_hour.get())
                    time_edit[2] = time_edit[2]+1
                    check_edit = 1
                
            if  en_min.get() != '\0' and int(en_min.get()) >= 0 and (int(en_min.get()) <= 59):
                if int(en_min.get())>time_format.tm_min or (int(en_min.get())<=time_format.tm_min and en_hour.get() !=''):
                    time_edit[4] = int(en_min.get())
                    check_edit = 1    
                elif int(en_min.get())<=time_format.tm_min and en_hour.get() =='':
                    time_edit[4] = int(en_min.get())
                    time_edit[3] = time_edit[3]+1
                    check_edit = 1    
                
            time_edit = tuple(time_edit)
            time_edit = time.mktime(time_edit)
            DATA[select_item][4] = time_edit
            
            if check_edit == 1:
                edit.destroy()
                check_bill()
                
            else:
                tv_table.item(select_item, text='', values=(
                DATA[select_item][1], DATA[select_item][2], f'{time_format.tm_mday}/{time_format.tm_mon}/{time_format.tm_year}-{time_format.tm_hour}:{time_format.tm_min}', '-', '-', '-'))
                edit.destroy()

        btn_edit_data = Button(edit, text='???????????????', bg='white',
                               relief=FLAT, width=10, height=1, command=edit_data)
        btn_edit_data.place(x=65, y=170)
        edit.mainloop()

    def cal_prices(time):
        if time <= 60:
            return 0
        elif time > 60 and time <= 90:
            return 60
        elif time > 90 and time <= 120:
            return 120
        elif time > 120 and time <= 180:
            return 240
        elif time > 180 and time <= 300:
            return 300
        elif time > 300:
            return 801
        return

    def bill_screen(list):
        bill = Tk()
        bill.title('Omakasa-bill')
        bill.geometry("300x300+100+250")
        bill['bg'] = '#FD650D'
        frm_contain = Frame(bill, bg='white')

        lb_name = Label(frm_contain, bg='white', font=(
            "Arial", 13), text=f'?????????????????????????????? : {list[1]}  Omakasa', pady=5)
        lb_amount = Label(frm_contain, bg='white', font=(
            "Arial", 13), text=f'??????????????? : {list[2]} ??????', pady=5)
        time_format = time.localtime(float(list[3]))
        lb_checkin = Label(frm_contain, bg='white', font=(
            "Arial", 13), text=f'???????????????????????????????????? : {time_format.tm_mday}/{time_format.tm_mon}/{time_format.tm_year}-{time_format.tm_hour}:{time_format.tm_min}')
        time_format = time.localtime(float(list[4]))
        lb_checkout = Label(frm_contain, bg='white', pady=5, font=(
            "Arial", 13), text=f'???????????????????????????????????? : {time_format.tm_mday}/{time_format.tm_mon}/{time_format.tm_year}-{time_format.tm_hour}:{time_format.tm_min}')

        lb_price = Label(frm_contain, bg='white', pady=5, font=(
            "Arial", 13), text=f'???????????? : {list[5]} ?????????')
        lb_total_price = Label(frm_contain, bg='white', pady=5, font=(
            "Arial", 13), text=f'????????????????????? : {list[6]} ?????????')

        global admin
        lb_admin = Label(frm_contain, bg='white', font=(
            "Arial", 13), pady=10, text=f'???????????????????????????????????? : {list[0]}  ??????????????????????????????????????? : {list[7]}')
        lb_name.pack()
        lb_amount.pack()
        lb_checkin.pack()
        lb_checkout.pack()
        lb_price.pack()
        lb_total_price.pack()
        lb_admin.pack()
        btn_confirm = Button(frm_contain, command=bill.destroy, text='???????????????????????????', pady=5, font=(
            "Arial", 10), bg='#FD650D', fg='white', relief=FLAT, width=10, height=1)
        btn_confirm.pack()
        frm_contain.place(x=10, y=10, width=280, height=280)
        select_item = tv_table.selection()[0]
        tv_table.delete(select_item)
        bill.mainloop()

    def write_file(index,name):
        global INDEX
        f = open(f'Omakasa/Data/customer/{name}{INDEX}', 'a')
        for item in DATA[index]:
            t = f.write(str(item)+'\n')
        f.close()
        INDEX +=1
        f = open(f'Omakasa/Data/index.txt', 'w')
        f.write(str(INDEX))
        f.close()

    def generate_bill():
        if not len(tv_table.selection()):
            return
        select_item = int(tv_table.selection()[0])
        if DATA[select_item][6] != 0 and DATA[select_item][5] != 0:
            bill_screen(DATA[select_item])

    def check_bill():
        if not len(tv_table.selection()):
            return
        select_item = int(tv_table.selection()[0])
        if DATA[select_item][4] == 0:
            DATA[select_item][4] = time.time()
        time_format = time.localtime(DATA[select_item][3])
        time_out = time.localtime(DATA[select_item][4])

        delta_time = ((time_out.tm_hour-time_format.tm_hour)*60) + (time_out.tm_min-time_format.tm_min)

        DATA[select_item][5] = 199 + cal_prices(delta_time)
        DATA[select_item][6] = DATA[select_item][5]*DATA[select_item][2]

        tv_table.item(select_item, text='', values=(DATA[select_item][1], DATA[select_item][2], f'{time_format.tm_mday}/{time_format.tm_mon}/{time_format.tm_year}-{time_format.tm_hour}:{time_format.tm_min}',
                      f'{time_out.tm_mday}/{time_out.tm_mon}/{time_out.tm_year}-{time_out.tm_hour}:{time_out.tm_min}', DATA[select_item][5], DATA[select_item][6]))
        write_file(select_item,DATA[select_item][1])

    def new_login():
        main.destroy()
        Login_screen()

    def search_data():
        s = Search_box.get()
        if s == '':
            return
        f = open(f'Omakasa/Data/customer/{s}','r')
        global data_search
        data_search = f.read().split('\n')
        f.close()
        data_search.pop()
        print(data_search)
        bill_screen(data_search)

    def add_user_screen():
        add = Tk()
        add.title('Omakasa-add')
        add.geometry("200x160+600+250")
        add['bg'] = '#FD650D'

        frm_contain = Frame(add, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)
        lb = Label(add, text='????????????????????????????????????????????????', fg='#FD650D',
                   bg='white', font=("Arial bold", 14)).pack()

        frm_name = Frame(frm_contain, bg='#FD650D', pady=10)
        lb_name = Label(frm_name, text='Username', bg='white')
        en_name = Entry(frm_name, text='', width=13, font=("Arial", 14))
        frm_name.pack()
        lb_name.grid(column=0, row=0)
        en_name.grid(column=1, row=0)

        def add_user():
            f = open(f'Omakasa/Data/admin.txt', 'a')
            add_new = f.write('\n'+en_name.get())
            f.close()
            add.destroy()

        btn_add_data = Button(add, text='???????????????', bg='white',
                              relief=FLAT, width=10, height=1, command=add_user)
        btn_add_data.place(x=65, y=120)

        add.mainloop()
    # create MENU_BAR
    menu_bar = Menu(main)
    user_menu = Menu(menu_bar, tearoff=0)
    user_menu.add_command(label='Add User', command=add_user_screen)
    user_menu.add_command(label='Sign Out', command=new_login)
    user_menu.add_command(label='Exit', command=main.destroy)

    menu_bar.add_cascade(label="User", menu=user_menu)

    # create LOGO
    Logo_txt = Label(main, text='OMAKASA', font=("Arial Bold", 45),
                     background="#FD650D", fg='white').place(x=10, y=10)
    fr = Frame(main, bg='white', width=300, height=3)
    fr.place(x=15, y=75)

    # create BTN & SEARCHBOX
    frm_contain_btn = Frame(main, bg='white', width=60, height=80,)
    global btn_add
    btn_add = Button(frm_contain_btn, text='???????????????', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#2ff764',
                     fg='white', bd=2, activebackground='#2ff764', activeforeground='white', command=add_screen)
    global btn_edit
    btn_edit = Button(frm_contain_btn, text='???????????????', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#fceb4c', fg='white', command=edit_screen
                      )
    global btn_del
    btn_del = Button(frm_contain_btn, text='??????', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#ed3737', fg='white', command=remove_screen
                     )

    frm_contain_btn.place(x=485, y=135)
    btn_add.grid(column=0, row=0)
    btn_edit.grid(column=1, row=0)
    btn_del.grid(column=2, row=0)

    Search_box = Entry(main, font=(
        "Arial", 16), width=20)
    Search_box.place(x=370, y=95)
    Search_button = Button(main, text='???????????????', font=(
        "Arial Bold", 13), background="#FD650D", fg='white', command=search_data).place(x=620, y=92)

    # create TABLE
    frm_table = Frame(main, bg="white")
    frm_table.place(width=633, height=350, x=43, y=175)

    tv_table = ttk.Treeview(frm_table)
    tv_table['columns'] = ('Name', 'Amount',
                           'CheckIn', 'CheckOut', 'Price', 'Total')

    tv_table.heading('#0', text='', anchor=CENTER)
    tv_table.heading('Name', text='Name', anchor=CENTER)
    tv_table.heading('Amount', text='Amount', anchor=CENTER)
    tv_table.heading('CheckIn', text='CheckIn', anchor=CENTER)
    tv_table.heading('CheckOut', text='CheckOut', anchor=CENTER)
    tv_table.heading('Price', text='Price', anchor=CENTER)
    tv_table.heading('Total', text='Total', anchor=CENTER)

    tv_table.column('#0', width=0, stretch=NO)
    tv_table.column('Name', anchor=CENTER, width=160)
    tv_table.column('Amount', anchor=CENTER, width=60)
    tv_table.column('CheckIn', anchor=CENTER, width=125)
    tv_table.column('CheckOut', anchor=CENTER, width=125)
    tv_table.column('Price', anchor=CENTER, width=80)
    tv_table.column('Total', anchor=CENTER, width=80)
    tv_table.place(x=0, y=0, height=350)

    btn_check_bill = Button(main, width=10, height=1, fg='white', bg='#FD650D',
                            text="?????????????????????", font=('Arail bold', 15), command=check_bill)
    btn_check_bill.place(x=557, y=540)

    btn_generate_bill = Button(main, width=10, height=1,
                               text="?????????????????????", font=('Arail bold', 15), command=generate_bill)
    btn_generate_bill.place(x=420, y=540)

    main.config(menu=menu_bar)
    main.mainloop()

pull_index()
# Login_screen()
main_screen()

