from tkinter import *
import pandas as pd
from pandas import DataFrame
from random import random
from tkinter import messagebox


# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
VOCAB_FONT = ("Ariel", 60, "bold")

# Create Dataframe from French words csv
french_dict = DataFrame.to_dict(orient="records")

# ---------------------------- Card Manager ------------------------------- #

def x_button_click():
    with open("data/french_words.csv", "R") as data_file:
        pd.read_csv(data_file)



        # canvas.vocab_text.get()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Cardy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Create French language title text
canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)

# Create vocab word text
vocab_text = canvas.create_text(400, 263, text="Word", font=VOCAB_FONT)

# Create the unknown x button
x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

# Create the known check button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=x_button_click)
known_button.grid(column=1, row=1)



# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop to display the window and handle user interactions
window.mainloop()

