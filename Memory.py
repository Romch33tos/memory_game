from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
import random
import shutil

cards = [
    "game_files/c1.jpg",
    "game_files/c2.jpg",
    "game_files/c3.jpg",
    "game_files/c4.jpg",
    "game_files/c5.jpg",
    "game_files/c6.jpg"
]

cards = cards * 2
random.shuffle(cards)

first_choice = None
second_choice = None
first_button = None
second_button = None
w = 0
buttons = []
images = []
can_click = False

def delete():
    shutil.rmtree("game_files")
    root.destroy()

def start():
    global w, first_choice, second_choice, first_button, second_button, can_click
    w = 0
    first_choice = None
    second_choice = None
    can_click = False
    
    for btn in buttons:
        btn.config(image=c0, state=NORMAL)

        for btn in buttons:
            btn.config(image=c0)
            root.after(100, show_all_cards) 

def show_all_cards():
    for btn in buttons:
        idx = buttons.index(btn)
        btn.config(image=images[idx])
    root.after(3000, hide)

def hide():
    for index in range(len(buttons)):
        buttons[index].config(image=c0)
    global can_click
    can_click = True  

def on_button_click(index):
    global first_choice, second_choice, first_button, second_button, can_click

    if not can_click:
        return  

    button = buttons[index]
    button.config(image=images[index])

    if first_choice is None:
        first_choice = cards[index]
        first_button = button
    elif second_choice is None:
        second_choice = cards[index]
        second_button = button
        can_click = False  
        root.after(750, check_match)

def check_match():
    global first_choice, second_choice, first_button, second_button, w, can_click

    if first_choice == second_choice:
        w += 1
        first_button.config(state=DISABLED)
        second_button.config(state=DISABLED)
    else:
        first_button.config(image=c0)
        second_button.config(image=c0)

    first_choice = None
    second_choice = None
    first_button = None
    second_button = None
    can_click = True

root = Tk()
root.geometry('700x520')
root.resizable(width=0, height=0)
root.title("Memory")
root.configure(bg="white")

shutil.unpack_archive("game_files.zip", "game_files")

c0 = ImageTk.PhotoImage(file="game_files/c0.jpg")  
images = [ImageTk.PhotoImage(file=card) for card in cards]
buttons = []

for row in range(3):
    frame = Frame(root, bg="white")
    frame.pack()
    for col in range(4):
        index = row * 4 + col
        btn = Button(frame, width=165, height=165, bg="white", image=c0, command=lambda index=index: on_button_click(index), state=DISABLED)
        btn.pack(side=LEFT)
        buttons.append(btn)

start()

root.protocol("WM_DELETE_WINDOW", delete)
root.mainloop()
