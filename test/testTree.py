from tkinter import *
from tkinter import ttk

root = Tk()
root.title('PythonGuides')
root.geometry('700x300')
root['bg'] = '#fb0'

tv_table = ttk.Treeview(root)
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


tv_table.insert(parent='', index=0, iid=0, text='', values=(1, 'Vineet', '3','11/11/64 - 11.11','11/11/64 - 11.11','199','1990'))
tv_table.place(x=0,y=0)

root.mainloop()
