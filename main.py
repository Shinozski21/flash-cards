from tkinter import *
import random
import pandas as pd
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words to learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/1000 basic English words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_word, text=current_card["Japanese"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    window.after(3000, func=flip_card_1)


def flip_card_1():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)
#     canvas.config(command=flip_card_2)
#
# def flip_card_2():
#     canvas.itemconfig(card_title, text="Japanese", fill="black")
#     canvas.itemconfig(card_word, text=current_card["Japanese"], fill="black")
#     canvas.itemconfig(card_background, image=card_back)
#     canvas.config(command=flip_card_1)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words to learn.csv", index=False)

    next_card()

# def reset():
#     ask_reset = messagebox.askyesno(title="Reset", message="Do you want to reset?")
#     if ask_reset:
#
#         to_learn = data.to_dict(orient="records")
#         print(len(to_learn))
#         next_card()
#     else:
#         return

window = Tk()
window.title("1000 English/Japanese Basic Flashcards")
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card_1)

canvas = Canvas(height=526, width=800, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="text", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 80, "bold"))

canvas.grid(row=1, column=0, columnspan=5, )

# card_back = PhotoImage(file=)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=is_known, highlightthickness=0, background=BACKGROUND_COLOR,
                      highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=2, column=3)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0, background=BACKGROUND_COLOR,
                      highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=2, column=1)

flip_img = PhotoImage(file="images/flip.png")
flip_button = Button(image=flip_img, command=flip_card_1, highlightthickness=0, background=BACKGROUND_COLOR,
                      highlightbackground=BACKGROUND_COLOR)
flip_button.grid(row=2, column=2)

# reset_img = PhotoImage(file="images/reset.png")
# reset_button = Button(image=reset_img, command=reset, highlightthickness=0, background=BACKGROUND_COLOR,
#                       highlightbackground=BACKGROUND_COLOR)
# reset_button.grid(row=0, column=0)

next_card()




window.mainloop()