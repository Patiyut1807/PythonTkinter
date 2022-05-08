import math
from tkinter import RIGHT, ttk
import tkinter as tk

window = tk.Tk()
window.geometry("400x450")
window.config(bg="#065489")

window.resizable(width=False, height=False)

window.title('Square Root Calculator')


def update_result(text):
    result.configure(text=text)


def calculate():
    if not numeral_form.get().isdigit():
        return
    result = math.sqrt(eval(numeral_form.get()))
    update_result(f'Result :{result:.2f}')
    history_treeview.insert(
        '', tk.END, values=[numeral_form.get(), f'{result:.2f}'])


def clear_tree():
    for i in history_treeview.get_children():
        history_treeview.delete(i)


title = tk.Label(window, text="Square Root", font=(
    "Arial", 24), fg="#fffcbd", bg="#065569")

numeral_lb = tk.Label(window, text="Numeral:", font=(
    "Arial", 12), fg="#fffcbd", bg="#065569")

result = tk.Label(window, text="Enter value to calculate", font=(
    "Arial", 12, "normal", "italic"), fg="White", bg="#065569", justify=tk.LEFT)

clear_button = tk.Button(window, text="Clear", font=(
    "Arial", 12, "bold"), fg="Black", bg="#29c70a", command=clear_tree)

calculate_button = tk.Button(window, text="Calculate", font=(
    "Arial", 13), fg="#13d675", bg="Black", command=calculate)

exit_button = tk.Button(window, text="Exit", font=(
    "Arial", 14), fg="White", bg="#b82741", command=exit)

columns = ('Numeral', 'Result')
history_treeview = ttk.Treeview(window, columns=columns, show="headings")
history_treeview.heading('Numeral', text='Numeral')
history_treeview.column("Numeral", minwidth=165,
                        width=165, stretch=False, anchor="c")
history_treeview.heading('Result', text='Result')
history_treeview.column("Result", minwidth=160,
                        width=160, stretch=False, anchor="c")


numeral = tk.StringVar()
numeral_form = tk.Entry(window, font=("Arial", 11),
                        textvariable=numeral, justify=RIGHT)

title.place(x=110, y=50)
numeral_lb.place(x=40, y=140)
numeral_form.place(x=120, y=140)
result.place(x=110, y=190)

calculate_button.place(x=290, y=135)
clear_button.place(x=313, y=190)
exit_button.place(height=35, width=75, x=290, y=410)
history_treeview.place(height=175, width=325, x=40, y=230)


window.mainloop()
