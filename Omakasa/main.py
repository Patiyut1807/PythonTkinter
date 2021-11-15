from tkinter import *

n=0
def main_screen():
    root = Tk()
    root.title('Omakasa')
    
    def add_row():
        global n
        frm_row = Frame(frm_table,width=650,height=15,pady=1,bg="#a8a5a5")
        frm_row.pack()
        table_n = Label(frm_row,text=n,font=("Arial", 13),width=2)
        customer = Label(frm_row,text='Patipan',font=("Arial", 13),width=15,bg='white')
        customer_n = Label(frm_row,text='5',font=("Arial", 13),width=3)
        checkIn = Label(frm_row,text='11/11/64-11:11',font=("Arial", 13),width=15,bg='white')
        checkOut = Label(frm_row,text='11/11/64-12:11',font=("Arial", 13),width=15)
        lb_price = Label(frm_row,text='500',font=("Arial", 13),padx='25',width=4,bg='white')
        btn_bill = Button(frm_row,text='เช็คบิล',padx=15,height=1,background="#49FF00")
        
        table_n.grid(column=0,row=0)
        customer.grid(column=1,row=0)
        customer_n.grid(column=2,row=0)
        checkIn.grid(column=3,row=0)
        checkOut.grid(column=4,row=0)
        lb_price.grid(column=5,row=0)
        btn_bill.grid(column=6,row=0)
        n+=1
    LogIn_txt = Label(root,text='OMAKASA',font=("Arial Bold", 45),background="#FD650D",fg='white').place(x=10,y=10)
    Search_box  = Entry(root,font=("Arial", 16),width=20).place(x=370,y=90)
        
    Search_button = Button(root,text='ค้นหา',font=("Arial Bold", 13),background="#FD650D",fg='white',command=add_row).place(x=620,y=87)

    frm_table = Frame(root,bg="white")
    frm_table.place(width=650,height=500,x=35,y=175)
    
    scr_bar = Scrollbar(frm_table)
    scr_bar.pack(side=RIGHT,fill=Y)
    root.geometry("720x720+300+0")
    root.mainloop() 
    
main_screen()