from tkinter import *
from turtle import bgcolor

# Constants
FONT_PRESS_START = "Press Start 2P"
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")

window.config(padx=20, pady=20, bg=BGCOLOR_DARKTHEME1)

canvas = Canvas(width=400, height=400, bg=BGCOLOR_DARKTHEME1, highlightthickness=0)

lock_img = PhotoImage(file="logo.png")

canvas.create_image(200, 200, image=lock_img)

canvas.grid(column=1, row=1)




# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)


# Start the main event loop to display the window and handle user interactions
window.mainloop()