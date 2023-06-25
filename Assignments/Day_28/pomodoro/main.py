import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
# Constants
FONT_PRESS_START = "Press Start 2P"
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps  # Global variable to track the number of repetitions
    reps += 1

    work_secs = WORK_MIN * 60  # Convert work duration from minutes to seconds
    short_break_secs = SHORT_BREAK_MIN * 60  # Convert short break duration from minutes to seconds
    long_break_secs = LONG_BREAK_MIN * 60  # Convert long break duration from minutes to seconds

    if reps % 8 == 0:
        # If it's the eighth repetition, start the long break countdown
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # If it's the second, fourth or sixth repetition,
        # start the work countdown
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks = "✔"
        checkmarks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()

# Set the title of the window
window.title("Pomodoro")

# Configure the window's padding and background color
window.config(padx=100, pady=50, bg=BGCOLOR_DARKTHEME2)

# Create a canvas for displaying the timer image and text
canvas = Canvas(width=200, height=224, bg=BGCOLOR_DARKTHEME2, highlightthickness=0)

# Load and display the tomato image on the canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Display the initial timer text on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_PRESS_START, 20, "normal"))

# Position the canvas in the window's grid
canvas.grid(column=1, row=1)

# Create a label for the timer
timer_label = Label(text="Timer", fg="green", bg=BGCOLOR_DARKTHEME2, font=(FONT_PRESS_START, 50, "normal"), padx=20, pady=20)

# Position the timer label in the window's grid
timer_label.grid(column=1, row=0)

# Create a label for displaying checkmarks
checkmarks_label = Label(fg="green", bg=BGCOLOR_DARKTHEME2, font=(FONT_PRESS_START, 20, "normal"), padx=20, pady=20)

# Position the checkmarks label in the window's grid
checkmarks_label.grid(column=1, row=4)

# Create a button for starting the timer
start_button = Button(text="Start", fg="orange", font=(FONT_PRESS_START, 8, "normal"), bg=BGCOLOR_DARKTHEME1, padx=5, pady=5, highlightthickness=0, command=start_timer)

# Position the start button in the window's grid
start_button.grid(column=0, row=3)

# Create a button for resetting the timer
reset_button = Button(text="Reset", fg="orange", font=(FONT_PRESS_START, 8, "normal"), bg=BGCOLOR_DARKTHEME1, padx=5, pady=5, highlightthickness=0, command=reset_timer)

# Position the reset button in the window's grid
reset_button.grid(column=2, row=3)





# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)


# Start the main event loop to display the window and handle user interactions
window.mainloop()