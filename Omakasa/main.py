from tkinter import *
def main_screen():
    root = Tk()
    root.title('Omakasa')
    
    LogIn_txt = Label(root,text='OMAKASA',font=("Arial Bold", 45),background="#FD650D",fg='white').place(x=10,y=3)
    Search_box  = Entry(root,font=("Arial", 16),width=20).place(x=370,y=90)
    Search_button = Button(root,text='ค้นหา',font=("Arial Bold", 13),background="#FD650D",fg='white').place(x=620,y=87)

    Container_costomer = Frame(root,bg="white")
    # label = Label(master=Container_costomer,text=' ',font=("Arial", 18)).grid(column=0,row=0)
    # label2 = Label(master=Container_costomer,text=' ' ,font=("Arial", 18)).grid(column=1,row=0,padx=50)
    Container_costomer.place(width=650,height=500,x=35,y=175)
    root.geometry("720x720+300+0")
    root.mainloop() 
    
main_screen()