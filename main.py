from tkinter import *
from tkinter import messagebox
from words import word_dict
from tkinter.ttk import *
import random
from threading import Thread
from time import sleep
import sys

word_number = 0
char_number = 0
wrongly_typed = []
check_num = 0


# defined working functions


def timer():
    for i in range(60):
        sleep(1)  # waits 60 seconds
    print(f"{word_number} in 60 seconds")
    user_entry.insert(END, string="Time up")
    user_entry.destroy()

    messagebox.showinfo(message=f'Your WPM is {word_number} and CPM is {char_number}',
                        title="Joshpydevops Speed Typing Test")
    sys.exit()


def start_timer():
    t1 = Thread(target=timer)
    user_entry.focus()
    t1.start()


def onkeypress(event):
    global word_number
    global char_number
    global check_num

    rimx = 0
    # if event.char:
    #

    # when space bar is clicked, check if user entry == to comp entry
    if event.char == " ":
        # streamline the values from the text and user entry to make it comparable.

        crossy = word_dict[check_num]
        crossy = crossy.split("\n")
        crossy = crossy[0]
        user_cross = user_entry.get()
        user_cross = user_cross[:-1]

        # Check if the values are the same and word count
        if user_cross.lower() == crossy.lower():
            word_number += 1
            char_number += len(user_cross)
        else:
            wrongly_typed.append(crossy.lower())
            wrongly_typed.append(user_cross.lower())

        # get hold of the text in the text box

        if len(crossy) + 1 < 10:
            rimx = 1.0 + ((len(crossy) + 1) / 10)

        elif len(crossy) + 1 >= 10:
            rimx = str(1.0 + round(((len(crossy) + 1) / 100), 2))

        check_num += 1

        # Delete the typed values and make space for new ones
        entry_comp.delete("1.0", rimx)
        user_entry.delete(0, END)

        print(crossy)


# ______ Root Setup ______

window = Tk()
window.title("Joshpydevops Speed Typing Test")
window.config(pady=50, padx=50, background="#222123")

label = Label(text='Joshpydevops Speed Typing Test', padding=10, font=("Arial", 25), foreground="crimson",
              background="#222123")
label.grid(column=0, row=1)

info = Label(
    text='How fast do you type? Want to test yourself? Do the one minute typing test below to find out. After every '
         'word, press the spacebar to go to the next word. Start at the red highlighted word.',
    padding=20, font=("Arial", 10, "italic"), wraplength=450, background="#222123", foreground="#eee3de")
info.grid(column=0, row=2)

# _______________ Text ______________________
x = 0
entry_comp = Text(height=9, width=90, wrap="word", background="#222123", foreground="#eee3de")
random.shuffle(word_dict)
cross = word_dict[check_num]
entry_comp.insert("1.0", word_dict)

if len(cross) + 1 < 10:
    x = 1.0 + ((len(cross) + 1) / 10)
elif len(cross) + 1 >= 10:
    t = (len(cross) + 1) / 100
    x = str(1.00 + round(t, 2))

entry_comp.tag_add(cross, "1.0", x)
entry_comp.tag_config(cross, background="red")
entry_comp.grid(column=0, row=4, pady=20, padx=20)
entry_comp.configure(font=("Arial", 10, "bold"))

style = Style()
style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), background="#eee3de", foreground="#222123")

l_type = Button(text='Click here to start', padding=10, command=start_timer, style="W.TButton")
l_type.grid(column=0, row=5)

user_entry = Entry(width=80, background="#eee3de", foreground="#222123")
user_entry.grid(column=0, row=6)
window.bind('<KeyPress>', onkeypress)

window.mainloop()
