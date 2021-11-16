from tkinter import *
from tkinter import ttk
import time

count = 0
def main_screen():
    main = Tk()
    main.title('Omakasa')
    main.geometry("720x720+300+0")
    #----------------------------------------------------------------
    def add_screen():
        add = Tk()
        add.title('Omakasa-insert')
        add.geometry("200x160+600+150")
        add['bg']='#FD650D'
    
        frm_contain = Frame(add,bg='#FD650D',width=180,height=150)
        frm_contain.place(x=5,y=25)
       
        frm_name = Frame(frm_contain,bg='#FD650D',pady=10)
        lb_name = Label(frm_name,text='Name',bg='white')
        en_name = Entry(frm_name,text='',width=13,font=("Arial",14))
        frm_name.pack()
        lb_name.grid(column=0,row=0)
        en_name.grid(column=1,row=0)
    
        frm_amount = Frame(frm_contain,bg='#FD650D',pady=10)
        lb_amount = Label(frm_amount,text='Amount',bg='white')
        en_amount = Entry(frm_amount,text='',width=12,font=("Arial",14))
        frm_amount.pack()
        lb_amount.grid(column=0,row=0)
        en_amount.grid(column=1,row=0)
        def add_data():
            global count
            t = time.localtime(time.time())
            tv_table.insert(parent='', index='end', iid=count, text='', values=(count,en_name.get(), en_amount.get(),f'{t.tm_mday}/{t.tm_mon}/{t.tm_year}-{t.tm_hour}:{t.tm_min}','-','-','-'))
            count+=1
            add.destroy()
        btn_add_data = Button(add,text='เพิ่ม',bg='white',relief=FLAT,width=10,height=1,command=add_data)
        btn_add_data.place(x=65,y=120)
    
        add.mainloop()
    #-----------------------------------------------------------------
    Logo_txt = Label(main,text='OMAKASA',font=("Arial Bold", 45),background="#FD650D",fg='white').place(x=10,y=10)
    
    frm_contain_btn = Frame(main,bg='white',width=60,height=80,)
    btn_add = Button(frm_contain_btn,text='เพิ่ม',font=("Arial bold", 12),relief=RIDGE,width=5,bg='#2ff764',fg='white',bd=2,command=add_screen)
    btn_edit = Button(frm_contain_btn,text='แก้ไข',font=("Arial bold", 12),relief=RIDGE,width=5,bg='#fceb4c',fg='white',state=DISABLED)
    btn_del = Button(frm_contain_btn,text='ลบ',font=("Arial bold", 12),relief=RIDGE,width=5,bg='#ed3737',fg='white',state=DISABLED)
    
    frm_contain_btn.place(x=485,y=135)
    btn_add.grid(column=0,row=0)
    btn_edit.grid(column=1,row=0)
    btn_del.grid(column=2,row=0)
    
    text_search = StringVar()
    Search_box  = Entry(main,textvariable=text_search, font=("Arial", 16),width=20).place(x=370,y=95) 
    Search_button = Button(main,text='ค้นหา',font=("Arial Bold", 13),background="#FD650D",fg='white').place(x=620,y=92)
    
    frm_table =Frame(main, bg="white")
    frm_table.place(width=640, height=500, x=30, y=175)
    
    tv_table = ttk.Treeview(frm_table)
    tv_table['columns'] = ('No.', 'Name', 'Amount', 'CheckIn','CheckOut', 'Price', 'Total')

    tv_table.heading('#0', text='', anchor=CENTER)
    tv_table.heading('No.', text='No', anchor=CENTER)
    tv_table.heading('Name', text='Name', anchor=CENTER)
    tv_table.heading('Amount', text='Amount', anchor=CENTER)
    tv_table.heading('CheckIn', text='CheckIn', anchor=CENTER)
    tv_table.heading('CheckOut', text='CheckOut', anchor=CENTER)
    tv_table.heading('Price', text='Price', anchor=CENTER)
    tv_table.heading('Total', text='Total', anchor=CENTER)

    tv_table.column('#0', width=0, stretch=NO)
    tv_table.column('No.', anchor=CENTER,width=25)
    tv_table.column('Name', anchor=CENTER, width=150)
    tv_table.column('Amount', anchor=CENTER, width=60)
    tv_table.column('CheckIn', anchor=CENTER, width=120)
    tv_table.column('CheckOut', anchor=CENTER, width=120)
    tv_table.column('Price', anchor=CENTER, width=80)
    tv_table.column('Total', anchor=CENTER, width=80)
    tv_table.place(x=0,y=0)
    
    fr = Frame(main,bg='white',width=300,height=3)
    fr.place(x=15,y=75)
    
    
#--------------------------------------------
    
    
    
    
    
#--------------------------------------------
    
    main.mainloop() 
    
main_screen()