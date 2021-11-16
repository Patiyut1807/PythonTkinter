from tkinter import *
#----- add_row func-----------------------
n=0
def main_screen():
    root = Tk()
    root.title('Omakasa')
    cv_table = Canvas(root)
    def add_row():
        global n
        frm_row = Frame(frm_table,width=660,height=15,pady=1,bg="#a8a5a5")
        frm_row.pack()
        table_n = Label(frm_row,text=n,font=("Arial", 13),width=3)
        customer = Label(frm_row,text='Patipan',font=("Arial", 13),width=15,bg='white')
        customer_n = Label(frm_row,text='5',font=("Arial", 13),width=3)
        checkIn = Label(frm_row,text='11/11/64-11:11',font=("Arial", 13),width=13,bg='white')
        checkOut = Label(frm_row,text='11/11/64-12:11',font=("Arial", 13),width=13)
        lb_price = Label(frm_row,text='11500',font=("Arial", 13),padx='25',width=1,bg='white')
        lb_total_price = Label(frm_row,text='11500',font=("Arial", 13),padx='25',width=1)
        btn_bill = Button(frm_row,text='เช็คบิล',padx=15,height=1,background="#49FF00")
        
        table_n.grid(column=0,row=0)
        customer.grid(column=1,row=0)
        customer_n.grid(column=2,row=0)
        checkIn.grid(column=3,row=0)
        checkOut.grid(column=4,row=0)
        lb_price.grid(column=5,row=0)
        lb_total_price.grid(column=6,row=0)
        btn_bill.grid(column=7,row=0)
        n+=1
    #----------------------------------------------------------------
    
    Logo_txt = Label(root,text='OMAKASA',font=("Arial Bold", 45),background="#FD650D",fg='white').place(x=10,y=10)
    
    frm_contain_btn = Frame(root,bg='white',width=60,height=80)
    btn_add = Button(frm_contain_btn,text='เพิ่ม',font=("Arial", 10),relief=FLAT,width=5,bg='green',pady=2)
    btn_edit = Button(frm_contain_btn,text='แก้ไข',font=("Arial", 10),relief=FLAT,width=5,bg='white',pady=2)
    btn_del = Button(frm_contain_btn,text='ลบ',font=("Arial", 10),relief=FLAT,width=5,bg='white',pady=2)
    
    frm_contain_btn.place(x=650,y=5)
    btn_add.grid(column=0,row=0)
    btn_edit.grid(column=0,row=1)
    btn_del.grid(column=0,row=2)
    
    text_search = StringVar()
    Search_box  = Entry(root,textvariable=text_search, font=("Arial", 16),width=20).place(x=370,y=95) 
    Search_button = Button(root,text='ค้นหา',font=("Arial Bold", 13),background="#FD650D",fg='white',command=add_row).place(x=620,y=92)

    fr = Frame(root,bg='white',width=300,height=3)
    fr.place(x=15,y=80)
    
    frm_topic = Frame(root,bg='white',width=670,height=75,bd=2)
    frm_topic.place(x=25,y=130)
    
    table_n = Label(frm_topic,text='ลำดับ',font=("Arial", 13),width=3,wraplength= 20,bg='white',height=2)
    customer = Label(frm_topic,text='ชื่อ',font=("Arial", 13),width=15,height=2)
    customer_n = Label(frm_topic,text='จำ นวน',font=("Arial", 13),width=3,wraplength= 30,bg='white',height=2)
    checkIn = Label(frm_topic,text='เวลาเข้า',font=("Arial", 13),width=13,height=2)
    checkOut = Label(frm_topic,text='เวลาออก',font=("Arial", 13),width=13,height=2,bg='white')
    lb_price = Label(frm_topic,text='ราคา/หัว',font=("Arial", 13),padx='25',width=1,height=2)
    lb_total_price = Label(frm_topic,text='ราคารวม',font=("Arial", 13),padx='25',width=1,height=2,bg='white')
    
    table_n.grid(column=0,row=0)
    customer.grid(column=1,row=0)
    customer_n.grid(column=2,row=0)
    checkIn.grid(column=3,row=0)
    checkOut.grid(column=4,row=0)
    lb_price.grid(column=5,row=0)
    lb_total_price.grid(column=6,row=0)
    
    
    frm_table = Frame(root,bg="white")
    frm_table.place(width=670,height=500,x=25,y=175)
    
    scr_bar = Scrollbar(frm_table)
    scr_bar.pack(side=RIGHT,fill=Y)
    root.geometry("720x720+300+0")
    root.mainloop() 
    
main_screen()