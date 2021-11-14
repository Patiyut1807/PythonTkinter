from tkinter import *
root = Tk()
root.title('Omakasa')


LogIn_txt = Label(root,text='Omakasa',font=("Arial Bold", 25)).place(x=0,y=0)
Search_box  = Entry(root,font=("Arial", 18)).place(x=350,y=60)
Search_button = Button(root,text='ค้นหา',font=("Arial Bold", 15)).place(x=620,y=55)


    
root.geometry("720x720+300+0")
root.mainloop() 