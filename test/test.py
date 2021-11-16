import tkinter as tk

focus = 0

def focus_in(event):
    global focus
    focus += 1

def focus_out(event):
    global focus
    focus -= 1
    if focus == 0:
        root.destroy()

root = tk.Toplevel()
root.bind("<FocusIn>", focus_in)
root.bind("<FocusOut>", focus_out)
root.mainloop()