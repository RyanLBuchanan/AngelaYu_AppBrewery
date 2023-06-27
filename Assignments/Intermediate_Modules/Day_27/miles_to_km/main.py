from tkinter import *

# Constants
FONT = ("Press Start 2P", 12, "normal")
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"

# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Create Tkinter window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=40, pady=40)

# Output label
output_label = Label(text="0", font=FONT)
output_label.grid(column=2, row=1)
output_label.config(padx=10, pady=10)

# Miles label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)

# Equal label
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=1, row=1)
equal_label.config(padx=10, pady=10)

# Km label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=3, row=1)
km_label.config(padx=10, pady=10)

# Button click function
def button_clicked():
    user_input = int(miles_input.get())
    output_label["text"] = round(user_input * 1.60934, 1)


# Calculate button
calculate_button = Button(text="Calculate", font=FONT, command=button_clicked)
calculate_button.grid(column=2, row=4)
calculate_button.config(padx=10, pady=10)

# Input field
miles_input = Entry(width=10, font=FONT, fg="white", bg="#92A8A0")
miles_input.grid(column=2, row=0)

# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop
window.mainloop()
