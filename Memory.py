from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import ImageTk
import random
import shutil

cards = ["Python/Программы/Игры/Memory/game_files/c1.jpg", "Python/Программы/Игры/Memory/game_files/c2.jpg","Python/Программы/Игры/Memory/game_files/c3.jpg","Python/Программы/Игры/Memory/game_files/c4.jpg", "Python/Программы/Игры/Memory/game_files/c5.jpg", "Python/Программы/Игры/Memory/game_files/c6.jpg"]

k = 0
k = 0
w = 0

def delete():
    shutil.rmtree("Python/Программы/Игры/Memory/game_files")
    root.destroy()

#Начало игры

def start():
    st.config(text = "", state = DISABLED)
    btn1.config(image = c1)
    btn2.config(image = c2)
    btn3.config(image = c3)
    btn4.config(image = c4)
    btn5.config(image = c5)
    btn6.config(image = c6)
    btn7.config(image = c1)
    btn8.config(image = c2)
    btn9.config(image = c3)
    btn10.config(image = c4)
    btn11.config(image = c5)
    btn12.config(image = c6)
    root.after(3000, hide)
    
def hide():
    btn1.config(image = c0, command = lambda: press1())
    btn2.config(image = c0, command = lambda: press2()) 
    btn3.config(image = c0, command = lambda: press3())
    btn4.config(image = c0, command = lambda: press4())
    btn5.config(image = c0, command = lambda: press5())
    btn6.config(image = c0, command = lambda: press6())
    btn7.config(image = c0, command = lambda: press7())
    btn8.config(image = c0, command = lambda: press8())
    btn9.config(image = c0, command = lambda: press9())
    btn10.config(image = c0, command = lambda: press10())
    btn11.config(image = c0, command = lambda: press11()) 
    btn12.config(image = c0, command = lambda: press12())   

def press1():
    global k
    k = 1
    btn1.config(image = c1)
    root.after(750, check1)
    
def press2():
    global k
    k = 2
    btn2.config(image = c2)
    root.after(750, check2)

def press3():
    global k
    k = 3
    btn3.config(image = c3)
    root.after(750, check3)

def press4():
    global k
    k = 4
    btn4.config(image = c4)
    root.after(750, check4)
       
def press5():
    global k
    k = 5
    btn5.config(image = c5)
    root.after(750, check5)
    
def press6():
    global k
    k = 6
    btn6.config(image = c6)
    root.after(750, check6)       
def press7():
    global r
    r = 1
    btn7.config(image = c1)
    root.after(750, check7)

def press8():
    global r
    r = 2
    btn8.config(image = c2)
    root.after(750, check8)      
def press9():
    global r
    r = 3
    btn9.config(image = c3)
    root.after(750, check9)   
    
def press10():
    global r
    r = 4
    btn10.config(image = c4)
    root.after(750, check10)     
def press11():
    global r
    r = 5
    btn11.config(image = c5)
    root.after(750, check11) 
    
def press12():
    global r
    r = 6
    btn12.config(image = c6)
    root.after(750, check12) 
     
def check1():   
    global k, r, w
    if k == 1 and r == 1:
        w += 1
        win()
        btn1.config(image = c1, state = DISABLED)
        btn7.config(image = c1, state = DISABLED)
    if k != 1 or r != 1:
        btn1.config(image = c0)
        k = 0

def check2():    
    global k, r, w
    if k == 2 and r == 2:
        w += 1
        win()
        btn2.config(image = c2, state = DISABLED)
        btn8.config(image = c2, state = DISABLED)
    if k != 2 or r != 2:
        btn2.config(image = c0)  
        k = 0
        
def check3():   
    global k, r, w
    if k == 3 and r == 3:
        w += 1
        win()
        btn3.config(image = c3, state = DISABLED)
        btn9.config(image = c3, state = DISABLED)
    if k != 3 or r != 3:
        btn3.config(image = c0)
        k = 0
        
def check4():   
    global k, r, w
    if k == 4 and r == 4:
        w += 1
        win()
        btn4.config(image = c4, state = DISABLED)
        btn10.config(image = c4, state = DISABLED)
    if k != 4 or r != 4:
        btn4.config(image = c0)
        k = 0
        
def check5():    
    global k, r, w
    if k == 5 and r == 5:
        w += 1
        win()
        btn5.config(image = c5, state = DISABLED)
        btn11.config(image = c5, state = DISABLED)
    if k != 5 or r != 5:
        btn5.config(image = c0)  
        k = 0
        
def check6():    
    global k, r, w
    if k == 6 and r == 6:
        w += 1
        win()
        btn6.config(image = c6, state = DISABLED)
        btn12.config(image = c6, state = DISABLED)    
    if k != 6 or r != 6:
        btn6.config(image = c0)
        k = 0
                 
def check7():
    global k, r, w
    if k == 1 and r == 1:
        w += 1
        win()
        btn1.config(image = c1, state = DISABLED)
        btn7.config(image = c1, state = DISABLED)
    if k != 1 or r != 1:
        btn7.config(image = c0)
        r = 0
               
def check8():
    global k, r, w
    if k == 2 and r == 2:
        w += 1
        win()
        btn2.config(image = c2, state = DISABLED)
        btn8.config(image = c2, state = DISABLED)
    if k != 2 or r != 2:
        btn8.config(image = c0) 
        r = 0
            
def check9():
    global k, r, w
    if k == 3 and r == 3:
        w += 1
        win()
        btn3.config(image = c3, state = DISABLED)
        btn9.config(image = c3, state = DISABLED)
    if k != 3 or r != 3:
        btn9.config(image = c0)
        r = 0
        
def check10():
    global k, r, w
    if k == 4 and r == 4:
        w += 1
        win()
        btn4.config(image = c4, state = DISABLED)
        btn10.config(image = c4, state = DISABLED)      
    if k != 4 or r != 4:
        btn10.config(image = c0)
        r = 0
        
def check11():
    global k, r, w
    if k == 5 and r == 5:
        w += 1
        win()
        btn5.config(image = c5, state = DISABLED)
        btn11.config(image = c5, state = DISABLED)
    if k != 5 or r != 5:
        btn11.config(image = c0)
        r = 0
                
def check12():
    global k, r, w
    if k == 6 and r == 6:
        w += 1
        win()
        btn6.config(image = c6, state = DISABLED)
        btn12.config(image = c6, state = DISABLED)
    if k != 6 or r != 6:
        btn12.config(image = c0)
        r = 0    
     
def win():
    global w
    if w == 12:
        st.configure(text = "Конец игры!", state = DISABLED, disabledforeground = "black")
        
#Графический интерфейс

root = Tk()
root.geometry('690x600')
root.resizable(width = 0, height = 0)
root.title("Memory")
root.configure(bg = "white")

shutil.unpack_archive("Python/Программы/Игры/Memory/game_files.zip", "Python/Программы/Игры/Memory/game_files")

#Выбор карточек

k1 = random.choice(cards)
c1 = ImageTk.PhotoImage(file = k1)
cards.remove(k1)

k2 = random.choice(cards)
c2 = ImageTk.PhotoImage(file = k2)
cards.remove(k2)

k3 = random.choice(cards)
c3 = ImageTk.PhotoImage(file = k3)
cards.remove(k3)

k4 = random.choice(cards)
c4 = ImageTk.PhotoImage(file = k4)
cards.remove(k4)

k5 = random.choice(cards)
c5 = ImageTk.PhotoImage(file = k5)
cards.remove(k5)

k6 = random.choice(cards)
c6 = ImageTk.PhotoImage(file = k6)
cards.remove(k6)

c0 = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/c0.jpg")

m = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/m.jpg")

e = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/e.jpg")

o = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/o.jpg")

r = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/r.jpg")

y = ImageTk.PhotoImage(file = "Python/Программы/Игры/Memory/game_files/y.jpg")

#Виджеты

frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)
frame2.pack()

frame3 = Frame(root)
frame3.pack()

btn1 = Button(frame1, width = 165, height = 165, bg = "white", image = m)


btn2 = Button(frame1, width = 165, height = 165, bg = "white", image = e)

btn3 = Button(frame1, width = 165, height = 165, bg = "white", image = c0)

btn4 = Button(frame1, width = 165, height = 165, bg = "white", image = c0)

btn5 = Button(frame2, width = 165, height = 165, bg = "white", image = c0)

btn6 = Button(frame2, width = 165,  height = 165, bg = "white", image = m)

btn7 = Button(frame2, width = 165, height = 165, bg = "white", image = o)

btn8 = Button(frame2, width = 165, height = 165, bg = "white", image = c0)

btn9 = Button(frame3, width = 165,  height = 165, bg = "white", image = c0)

btn10 = Button(frame3, width = 165,  height = 165, bg = "white", image = c0)

btn11 = Button(frame3, width = 165,  height = 165, bg = "white", image = r)

btn12 = Button(frame3, width = 165,  height = 165, bg = "white", image = y)

st = Button(root, width = 10, command = lambda: start(), bg = "white", text = "Играть!")

btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
btn3.pack(side = LEFT)
btn4.pack(side = LEFT)
btn5.pack(side = LEFT)
btn6.pack(side = LEFT)
btn7.pack(side = LEFT)
btn8.pack(side = LEFT)
btn9.pack(side = LEFT)
btn10.pack(side = LEFT)
btn11.pack(side = LEFT)
btn12.pack(side = LEFT)
st.pack(side = "bottom", pady = 10)

root.protocol("WM_DELETE_WINDOW", delete)

root.mainloop()