from tkinter import *
from tkinter import ttk
import time


count = 1
def main_screen():
    main = Tk()
    main.title('Omakasa')
    main.geometry("720x600+350+100")


    # ---------------------------------------------------------------

    def add_screen():
        add = Tk()
        add.title('Omakasa-insert')
        add.geometry("200x160+600+250")
        add['bg'] = '#FD650D'

        frm_contain = Frame(add, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)
        
        lb = Label(add,text='เพิ่มข้อมูล',fg='#FD650D',bg='white',font=("Arial bold",14)).pack()

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
            global count
            t = time.localtime(time.time())
            tv_table.insert(parent='', index='end', iid=count, text='', values=(count, en_name.get(
            ), en_amount.get(), f'{t.tm_mday}/{t.tm_mon}/{t.tm_year}-{t.tm_hour}:{t.tm_min}', '-', '-', '-'))
            count += 1
            add.destroy()
        btn_add_data = Button(add, text='เพิ่ม', bg='white',
                              relief=FLAT, width=10, height=1, command=add_data)
        btn_add_data.place(x=65, y=120)

        add.mainloop()

    def remove_screen():
        if not len(tv_table.selection()):
            return
        x = tv_table.selection()[0]

        def del_data():
            tv_table.delete(x)
            delete_promt.destroy()

        delete_promt = Tk()
        delete_promt.title('Omakasa-Delete')
        delete_promt.geometry("200x160+600+150")
        delete_promt['bg'] = 'white'

        lb_ask = Label(delete_promt, text='คุณต้องการ\nลบข้อมูลใช่หรือไม่?',
                       bg='white', font=("Arial", 13), pady=15)
        btn_confirm = Button(delete_promt, text='ตกลง',
                             command=del_data, width=7, height=2)
        btn_cancel = Button(delete_promt, text='ยกเลิก',
                            width=7, height=2, command=delete_promt.destroy)

        lb_ask.pack(pady=10)
        btn_confirm.pack(side=LEFT, padx=20)
        btn_cancel.pack(side=RIGHT, padx=20)

    def edit_screen():
        if not len(tv_table.selection()):
            return
        edit = Tk()
        edit.title('Omakasa-edit')
        edit.geometry("200x160+600+150")
        edit['bg'] = '#FD650D'
        frm_contain = Frame(edit, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)

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

        def edit_data():
            t=time.localtime(time.time())
            select_item = tv_table.selection()[0]
            tv_table.item(select_item,text='',values=(2, 'csddssd', 'dsadas',' ',f'{t.tm_mday}/{t.tm_mon}/{t.tm_year}-{t.tm_hour}:{t.tm_min}', '-', '-'))
        btn_edit_data = Button(edit,text='แก้ไข',bg='white',relief=FLAT,width=10,height=1,command=edit_data)
        btn_edit_data.place(x=65,y=120)
        edit.mainloop()

    def check_bill():
        if not len(tv_table.selection()):
            return

    # -----------------------------------------------------------------

    menu_bar = Menu(main)
    user_menu = Menu(menu_bar,tearoff=0)
    user_menu.add_command(label='Edit Username')
    user_menu.add_command(label='Sign Out',command=Login_screen)
    user_menu.add_command(label='Exit',command=main.destroy)

    menu_bar.add_cascade(label="User", menu=user_menu)

    Logo_txt = Label(main, text='OMAKASA', font=("Arial Bold", 45),
                     background="#FD650D", fg='white').place(x=10, y=10)
    fr = Frame(main, bg='white', width=300, height=3)
    fr.place(x=15, y=75)

    frm_contain_btn = Frame(main, bg='white', width=60, height=80,)
    global btn_add
    btn_add = Button(frm_contain_btn, text='เพิ่ม', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#2ff764',
                     fg='white', bd=2, activebackground='#2ff764', activeforeground='white', command=add_screen)
    global btn_edit
    btn_edit = Button(frm_contain_btn, text='แก้ไข', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#fceb4c', fg='white', command=edit_screen
                      )
    global btn_del
    btn_del = Button(frm_contain_btn, text='ลบ', font=("Arial bold", 12), relief=RIDGE, width=5, bg='#ed3737', fg='white', command=remove_screen
                     )

    frm_contain_btn.place(x=485, y=135)
    btn_add.grid(column=0, row=0)
    btn_edit.grid(column=1, row=0)
    btn_del.grid(column=2, row=0)

    text_search = StringVar()
    Search_box = Entry(main, textvariable=text_search, font=(
        "Arial", 16), width=20).place(x=370, y=95)
    Search_button = Button(main, text='ค้นหา', font=(
        "Arial Bold", 13), background="#FD650D", fg='white').place(x=620, y=92)

    frm_table = Frame(main, bg="white")
    frm_table.place(width=660, height=350, x=30, y=175)

    tv_table = ttk.Treeview(frm_table)
    tv_table['columns'] = ('No.', 'Name', 'Amount',
                           'CheckIn', 'CheckOut', 'Price', 'Total')

    tv_table.heading('#0', text='', anchor=CENTER)
    tv_table.heading('No.', text='No', anchor=CENTER)
    tv_table.heading('Name', text='Name', anchor=CENTER)
    tv_table.heading('Amount', text='Amount', anchor=CENTER)
    tv_table.heading('CheckIn', text='CheckIn', anchor=CENTER)
    tv_table.heading('CheckOut', text='CheckOut', anchor=CENTER)
    tv_table.heading('Price', text='Price', anchor=CENTER)
    tv_table.heading('Total', text='Total', anchor=CENTER)

    tv_table.column('#0', width=0, stretch=NO)
    tv_table.column('No.', anchor=CENTER, width=27)
    tv_table.column('Name', anchor=CENTER, width=160)
    tv_table.column('Amount', anchor=CENTER, width=60)
    tv_table.column('CheckIn', anchor=CENTER, width=125)
    tv_table.column('CheckOut', anchor=CENTER, width=125)
    tv_table.column('Price', anchor=CENTER, width=80)
    tv_table.column('Total', anchor=CENTER, width=80)
    tv_table.place(x=0, y=0, height=350)

    btn_check_bill = Button(main, width=10, height=1, fg='white', bg='#FD650D',
                            text="คิดเงิน", font=('Arail bold', 15), command=check_bill)
    btn_check_bill.place(x=570, y=540)

# --------------------------------------------


# --------------------------------------------
    main.config(menu=menu_bar)
    main.mainloop()
main_screen()