from tkinter import *
from tkinter import ttk

def add_screen():
    add = Tk()
    add.title('Omakasa-insert')
    add.geometry("200x160+600+150")
    add['bg']='#FD650D'
    
    frm_contain = Frame(add,bg='#FD650D',width=180,height=150)
    frm_contain.place(x=5,y=25)
    add_name = StringVar()
    frm_name = Frame(frm_contain,bg='#FD650D',pady=10)
    lb_name = Label(frm_name,text='Name',bg='white')
    en_name = Entry(frm_name,text='',width=13,textvariable=add_name,font=("Arial",14))
    frm_name.pack()
    lb_name.grid(column=0,row=0)
    en_name.grid(column=1,row=0)
    
    add_amount = StringVar()
    frm_amount = Frame(frm_contain,bg='#FD650D',pady=10)
    lb_amount = Label(frm_amount,text='Amount',bg='white')
    en_amount = Entry(frm_amount,text='',width=12,textvariable=add_amount,font=("Arial",14))
    frm_amount.pack()
    lb_amount.grid(column=0,row=0)
    en_amount.grid(column=1,row=0)
    
    btn_add_data = Button(add,text='เพิ่ม',bg='white',relief=FLAT,width=10,height=1)
    btn_add_data.place(x=65,y=120)
    
    add.mainloop()
add_screen()