def edit_screen():
        if not len(tv_table.selection()):
            return
        edit = Tk()
        edit.title('Omakasa-edit')
        edit.geometry("200x200+600+150")
        edit['bg'] = '#FD650D'
        frm_contain = Frame(edit, bg='#FD650D', width=180, height=150)
        frm_contain.place(x=5, y=25)
        lb = Label(edit, text='แก้ไขข้อมูล', fg='#FD650D',
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
        lb_mintxt = Label(frm_date, text='เวลานั่งทาน', bg='white', padx=1)
        lb_min = Label(frm_date, text='นาที', bg='white', padx=1)
        en_min = Entry(frm_date, text='', width=5, font=("Arial", 12))

        frm_date.pack()
        lb_mintxt.grid(column=2, row=1)
        en_min.grid(column=3, row=1)
        lb_min.grid(column=4, row=1)
        def edit_data():
            select_item = int(tv_table.selection()[0])
            
            if en_name.get() != '':
                changed_name = en_name.get()
                DATA[select_item][1] = changed_name
            if en_amount.get() != '':
                changed_amount = en_amount.get()
                DATA[select_item][2] = int(changed_amount)
                
            time_format = time.localtime(DATA[select_item][3])
            time_edit =  time_format
            time_edit = list((time_edit.tm_year, time_edit.tm_mon, time_edit.tm_mday, time_edit.tm_hour,time_edit.tm_min, time_edit.tm_sec, time_edit.tm_wday, time_edit.tm_yday, time_edit.tm_isdst))
            check_edit = 0
            if en_min.get().isdigit() and int(en_min.get())> 0 and int(en_min.get())<= 1440:
                time_edit[2]= time_edit[2]+int(en_min.get())//(24*60)
                time_edit[3]= time_edit[3]+(int(en_min.get())%(24*60))//60
                time_edit[4]= time_edit[4]+(int(en_min.get())%(24*60))%60
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

        btn_edit_data = Button(edit, text='แก้ไข', bg='white',
                               relief=FLAT, width=10, height=1, command=edit_data)
        btn_edit_data.place(x=65, y=170)
        edit.mainloop()