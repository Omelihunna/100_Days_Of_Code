from tkinter import *
# import json
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    datadict = {row.French: row.English for (index, row) in data.iterrows()}
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    datadict = {row.French: row.English for (index, row) in original_data.iterrows()}
    print(original_data)
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

french_words = list(datadict.keys())
french_word = choice(french_words)
timer = None


def change_word():
    global french_words, french_word, change_timer
    window.after_cancel(change_timer)
    french_word = choice(words_to_learn)
    front_card_canvas.itemconfig(front_card_img, image=flashcard_front_img)
    front_card_canvas.itemconfig(front_card_topic, text="French", fill="black")
    front_card_canvas.itemconfig(front_card_text, text=french_word["French"], fill="black")
    change_timer = window.after(3000, flip_card)


def flip_card():
    front_card_canvas.itemconfig(front_card_img, image=flashcard_back_img)
    front_card_canvas.itemconfig(front_card_topic, text="English", fill="white")
    front_card_canvas.itemconfig(front_card_text, text=french_word["English"], fill="white")

def is_known():
    words_to_learn.remove(french_word)
    data_words = pandas.DataFrame(words_to_learn)
    data_words.to_csv("data/words_to_learn.csv", index=False)
    change_word()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

change_timer = window.after(3000, flip_card)

flashcard_front_img = PhotoImage(file="./images/card_front.png")
flashcard_back_img = PhotoImage(file="./images/card_back.png")
right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")

front_card_canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = front_card_canvas.create_image(400, 263, image=flashcard_front_img)
front_card_topic = front_card_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
front_card_text = front_card_canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
front_card_canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

change_word()
window.mainloop()


# back_card_canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
# back_card_canvas.create_image(400, 263, image=flashcard_back_img)
# back_card_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
# back_card_canvas.create_text(400, 263, text="Content", font=("Ariel", 60, "bold"))
# back_card_canvas.grid(column=0, row=0, columnspan=2)