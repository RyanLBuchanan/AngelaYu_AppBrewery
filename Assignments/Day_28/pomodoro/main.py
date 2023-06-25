from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# Constants
FONT_PRESS_START = "Press Start 2P"
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BGCOLOR_DARKTHEME2)

canvas = Canvas(width=200, height=224, bg=BGCOLOR_DARKTHEME2, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_PRESS_START, 12, "normal"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg="yellow", bg=BGCOLOR_DARKTHEME2, font=(FONT_PRESS_START, 20, "normal"), padx=20, pady=20)

timer_label.grid(column=1, row=0)

checkmark_label = Label(text="✔", fg="yellow", bg=BGCOLOR_DARKTHEME2, font=(FONT_PRESS_START, 20, "normal"), padx=20, pady=20)

checkmark_label.grid(column=1, row=4)

start_button = Button(text="Start", font=(FONT_PRESS_START, 8, "normal"))

start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=(FONT_PRESS_START, 8, "normal"))

reset_button.grid(column=2, row=3)




# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)


# Start the main event loop to display the window and handle user interactions
window.mainloop()