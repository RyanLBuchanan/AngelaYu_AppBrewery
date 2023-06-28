from tkinter import *
import pandas as pd
from pandas import DataFrame
import random
from tkinter import messagebox

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
VOCAB_FONT = ("Ariel", 60, "bold")

# Global variables
current_card = {}
to_learn = {}

# ---------------------------- Card Manager ------------------------------- #
# Create Dataframe from French words csv
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") # Dictionary such that: [{'French': 'partie', 'English': 'part'}, . . . ,
    # {'French': 'histoire', 'English': 'history'}]



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Cardy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Call flip card function
flip_timer = window.after(3000, func=flip_card)

# Images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Create French language title text
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)

# Create vocab word text
card_word = canvas.create_text(400, 263, text="Word", font=VOCAB_FONT)

# Create the unknown x button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Create the known check button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# Add French word to replace the UI placeholders by calling the next_card() function
next_card()


# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop to display the window and handle user interactions
window.mainloop()
