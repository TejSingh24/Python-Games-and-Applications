from os import remove
from textwrap import fill
import tkinter as tk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
count = 0
flip_timer = None
current_card = {}

# ------------------------------------------------------ Reading Data ----------------------------------------------------------#
try:
    data = pd.read_csv('app_brewery-365 days code\\flash-card-project-start\\data\\words_to_learn.csv')
    dictionary = data.to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv('app_brewery-365 days code\\flash-card-project-start\\data\\french_words.csv')
    dictionary = data.to_dict(orient='records')



def pick():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(front_img, image=card_front)
    canvas.itemconfig(french_word, text=current_card['French'], fill='black')
    canvas.itemconfig(title, text='French', fill='black')
    flip_timer = window.after(3000, flip)


def know():
    global dictionary
    dictionary.remove(current_card)
    pd.DataFrame(dictionary).to_csv('app_brewery-365 days code\\flash-card-project-start\\data\\words_to_learn.csv', index=False)
    pick()


# ------------------------------------------------------ Flashing flash cards ----------------------------------------------------------#
def flip():
    canvas.itemconfig(front_img, image=card_back)
    canvas.itemconfig(french_word, text=current_card['English'], fill='white')
    canvas.itemconfig(title, text='English', fill='white')
    window.after_cancel(flip_timer)









# ------------------------------------------------------ UI ----------------------------------------------------------#
window = tk.Tk()
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file='app_brewery-365 days code\\flash-card-project-start\images\\card_front.png')
card_back = tk.PhotoImage(file='app_brewery-365 days code\\flash-card-project-start\images\\card_back.png')
front_img = canvas.create_image(401, 260, image=card_front)
title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
french_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

flip_timer = window.after(3000, flip)

pick()

canvas.grid(column=0, row=0, columnspan=2)


cross_img = tk.PhotoImage(file='app_brewery-365 days code\\flash-card-project-start\\images\\wrong.png')
wrong_button = tk.Button(image=cross_img, highlightthickness=0, command=pick)
wrong_button.grid(column=0, row=1)

right_img = tk.PhotoImage(file='app_brewery-365 days code\\flash-card-project-start\\images\\right.png')
right_button = tk.Button(image=right_img, highlightthickness=0, command=know)
right_button.grid(column=1, row=1)


window.mainloop()
