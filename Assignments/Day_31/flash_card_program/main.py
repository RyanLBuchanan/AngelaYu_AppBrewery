from tkinter import *
from tkinter import messagebox

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
VOCAB_FONT = ("Ariel", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
card_front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_front_canvas.create_image(0, 0, anchor= "nw", image=card_front_img)
card_front_canvas.grid(column=0, row=0, columnspan=2)

wrong_canvas = Canvas(width=300, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_canvas.create_image(0, 0, anchor= "nw", image=wrong_img)
wrong_canvas.grid(column=0, row=1)

right_canvas = Canvas(width=300, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
right_img = PhotoImage(file="images/right.png")
right_canvas.create_image(0, 0, anchor= "nw", image=right_img)
right_canvas.grid(column=1, row=1)

# Labels
# Labels

# Add language label
language_label = card_front_canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black", anchor="center")
# language_label = Label(text="Website:", fg="black", bg="white", font=LANGUAGE_FONT, highlightthickness=0)
# language_label.grid(column=0, row=1)  # Display the website label in column 0, row 2

# Add vocab label
vocab_label = card_front_canvas.create_text(400, 250, text="les mots", font=VOCAB_FONT, fill="black", anchor="center")
# vocab_label = Label(text="Email/Username:", fg="black", bg="white", font=VOCAB_FONT, highlightthickness=0)
# vocab_label.grid(column=0, row=2)  # Display the email label in column 0, row 3











# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop to display the window and handle user interactions
window.mainloop()

