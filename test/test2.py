from tkinter import *

root = Tk()
root.geometry("500x400")

main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar = Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

sec_frm = Frame(my_canvas)

my_canvas.create_window((0,0),window=sec_frm,anchor='nw')
for thing in range(59):
    Button(sec_frm,text=thing).grid(column=0,row=thing,pady=10,padx=10)

root.mainloop()