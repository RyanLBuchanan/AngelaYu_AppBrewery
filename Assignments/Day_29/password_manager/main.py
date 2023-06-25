from tkinter import *
from rich import padding

# Constants
FONT = ("Calibri", 12, "normal")
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg=BGCOLOR_DARKTHEME1, padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=BGCOLOR_DARKTHEME1, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)  # Display the canvas in column 1, spanning 4 rows

# Labels
website_label = Label(text="Website:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
website_label.grid(column=0, row=1)  # Display the website label in column 0, row 2

email_label = Label(text="Email/Username:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
email_label.grid(column=0, row=2)  # Display the email label in column 0, row 3

password_label = Label(text="Password:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
password_label.grid(column=0, row=3)  # Display the password label in column 0, row 4

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)  # Display the website entry field in column 1, row 2

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)  # Display the email entry field in column 1, row 3

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)  # Display the password entry field in the frame, with right padding

# Buttons
password_button = Button(text="Generate Password", fg="orange", bg=BGCOLOR_DARKTHEME2, font=("Calibri", 9, "normal"), highlightthickness=0)
password_button.grid(column=2, row=3)  # Display the password button in the frame, with left alignment

add_button = Button(width=50, text="Add", fg="orange", bg=BGCOLOR_DARKTHEME2, font=("Calibri", 9, "normal"), highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

# ---------------------------- Development Tools ------------------------------- #

# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop to display the window and handle user interactions
window.mainloop()
