from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
current_card = {}


def swipe():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(card_side, image=card_front)
    card.itemconfig(word, text=current_card["French"])
    card.itemconfig(title, text="French")
    flip_timer = window.after(3000, flip)


def flip():
    card.itemconfig(card_side, image=card_back)
    card.itemconfig(word, text=current_card["English"])
    card.itemconfig(title, text="English")


def remove():
    swipe()
    to_learn.remove(to_learn[to_learn.index(current_card)])
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    print(df)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# window.wm_attributes('-transparentcolor', '#ab23ff')

flip_timer = window.after(3000, flip)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_side = card.create_image(400, 263, image=card_front)
card.grid(column=0, row=0, columnspan=2)
title = card.create_text(400, 150, text="Title", font=("Aeriel", 40, "italic"))
word = card.create_text(400, 263, text="Word", font=("Aeriel", 60, "bold"))

right_button = Button(image=right, highlightthickness=0, command=remove)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=swipe)
wrong_button.grid(column=1, row=1)

swipe()

window.mainloop()