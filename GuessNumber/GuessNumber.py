import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#065569")

window.resizable(width=False, height=False)

window.title('Guess Number Game')

TARGET = random.randint(0, 100)
RETRIES = 0

def update_result(text):
    result.configure(text=text)


def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    number_form.delete(0,'end')
    TARGET = random.randint(0, 100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")


def play_game():
    global RETRIES
    if number_form.get().isdigit() and int(number_form.get())<=100 and int(number_form.get())>=0 :
        choice = int(number_form.get())
        if choice != TARGET:
            RETRIES += 1
            result = "Wrong Guess!! Try Again"
            if TARGET < choice:
                hint = "The guess number is less than {}".format(
                    choice)
            else:
                hint = "The guess number is more than {}".format(
                    choice)
            result += "\n\nHINT :\n" + hint

        else:
            result = "You guessed the correct number after {} retries".format(
                RETRIES)
            guess_button.configure(state='disabled')
            result += "\n" + "Click on Play to start a new game"
        update_result(result)
    else:
        number_form.delete(0,'end')

title = tk.Label(window, text="Guessing Game", font=(
    "Arial", 24), fg="#fffcbd", bg="#065569")

result = tk.Label(window, text="Click on Play to start a new game", font=(
    "Arial", 12, "normal", "italic"), fg="White", bg="#065569", justify=tk.LEFT)

play_button = tk.Button(window, text="Play Game", font=(
    "Arial", 14, "bold"), fg="Black", bg="#29c70a", command=new_game)

guess_button = tk.Button(window, text="Guess", font=(
    "Arial", 13), state='disabled', fg="#13d675", bg="Black", command=play_game)

exit_button = tk.Button(window, text="Exit Game", font=(
    "Arial", 14), fg="White", bg="#b82741", command=exit)

guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

title.place(x=170, y=50)
result.place(x=180, y=210)

exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

number_form.place(x=180, y=150)

window.mainloop()