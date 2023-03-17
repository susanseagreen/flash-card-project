from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words = "german_words"
phrases = "german_phrases"
die_der_das = "german_die_der_das"

data = pandas.read_csv("data/german_all.csv")
to_learn = data.to_dict(orient="records")

# Get language from csv
language = data.columns[1]

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=language, fill="black")
    canvas.itemconfig(card_word, text=current_card[language], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def flip_card(e):
    canvas.itemconfig(card_title, text="German", fill="white")
    canvas.itemconfig(card_word, text=current_card["German"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        wrong_btn.destroy()
        right_btn.destroy()
        canvas.itemconfig(card_title, text="Well Done!", fill="white")
        canvas.itemconfig(card_word, text="You have completed all\nthe flashcards correctly", fill="white")
    next_card()


window = Tk()
window.title("Study Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.bind("<space>", func=flip_card) and window.bind("<Button-1>", func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 50, text="", fill="black", font=("Ariel", 40, "italic"), width=650)
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "italic"), width=650)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
right_btn = Button(image=right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()
