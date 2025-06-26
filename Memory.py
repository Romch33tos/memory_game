from tkinter import *
from PIL import ImageTk, Image
import random
import os
import sys
from tkinter import messagebox

CARD_IMAGES = [
  "cat_card.png",
  "dog_card.png",
  "parrot_card.png",
  "hamster_card.png",
  "hamster2_card.png",
  "rabbit_card.png"
]

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

class MemoryGame:
  def __init__(self, master):
    self.master = master
    master.title("Memory")
    master.configure(bg="white")
    master.resizable(False, False)

    self.create_menu()

    self.card_pairs = CARD_IMAGES * 2
    random.shuffle(self.card_pairs)
    self.first_card = None
    self.second_card = None
    self.first_button = None
    self.second_button = None
    self.buttons = []
    self.images = []
    self.can_click = False
    self.matched_pairs = 0
    self.total_pairs = len(CARD_IMAGES)

    self.default_image = ImageTk.PhotoImage(Image.open(resource_path("empty_card.png")))
    self.load_images()
    self.create_board()
    self.start_game()

  def create_menu(self):
    menubar = Menu(self.master)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Как играть", command=self.show_help)
    menubar.add_cascade(label="Справка", menu=help_menu)

    self.master.config(menu=menubar)

  def show_help(self):
    help_text = """Правила игры
- В начале игры все карточки открыты на 3 секунды
- Затем они переворачиваются рубашкой вверх
- Нажимайте на карточки, чтобы открыть их
- Открывайте по две карточки за ход
- Если карточки совпадают - они остаются открытыми
- Если не совпадают - переворачиваются обратно
- Цель - найти все пары карточек
- После победы нажмите пробел для новой игры"""
    messagebox.showinfo("Справка", help_text)

  def load_images(self):
    self.images = [ImageTk.PhotoImage(Image.open(resource_path(card))) for card in self.card_pairs]

  def create_board(self):
    for row in range(3):  
      frame = Frame(self.master, bg="white")
      frame.pack()
      for col in range(4):  
        index = row * 4 + col
        button = Button(frame, width=100, height=100, bg="white", image=self.default_image,
                        command=lambda index=index: self.on_card_click(index))
        button.pack(side=LEFT)
        self.buttons.append(button)

  def start_game(self):
    self.card_pairs = random.sample(CARD_IMAGES * 2, 12)
    random.shuffle(self.card_pairs)
    self.load_images()

    self.first_card = None
    self.second_card = None
    self.matched_pairs = 0
    self.can_click = False

    for button in self.buttons:
      button.config(image=self.default_image, state=NORMAL)

    self.master.after(100, self.show_all_cards)

  def show_all_cards(self):
    for i, button in enumerate(self.buttons):
      button.config(image=self.images[i])
    self.can_click = False
    self.master.after(3000, self.hide_cards)

  def hide_cards(self):
    for button in self.buttons:
      button.config(image=self.default_image)
    self.can_click = True

  def on_card_click(self, index):
    if not self.can_click or self.buttons[index]['state'] == DISABLED:
      return

    button = self.buttons[index]
    button.config(image=self.images[index])

    if self.first_card is None:
      self.first_card = self.card_pairs[index]
      self.first_button = button
    elif self.second_card is None and button != self.first_button:
      self.second_card = self.card_pairs[index]
      self.second_button = button
      self.can_click = False
      self.master.after(750, self.check_match)

  def check_match(self):
    if self.first_card == self.second_card:
      self.first_button.config(state=DISABLED)
      self.second_button.config(state=DISABLED)
      self.matched_pairs += 1

      if self.matched_pairs == self.total_pairs:
        messagebox.showinfo("Вы нашли все пары!", "Нажмите пробел для новой игры.")
        self.master.bind('<space>', lambda event: self.start_game())
    else:
      self.first_button.config(image=self.default_image)
      self.second_button.config(image=self.default_image)

    self.first_card = None
    self.second_card = None
    self.first_button = None
    self.second_button = None
    self.can_click = True

root = Tk()
game = MemoryGame(root)
root.mainloop()
