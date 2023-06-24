from tkinter import *

FONT = ("Press Start 2P", 12, "normal")


# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


window = Tk()
window.title("Hello GUI")
window.minsize(width=900, height=700)
window.configure(bg="#1F3B4D")
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label.", font=FONT, fg="orange", bg="#92A8A0")

# Initialize
# my_label.pack()  # Alignment with "side="left"

# Change label text
my_label["text"] = "New text"
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
# Button click function
def button_clicked():
    user_input = input_field.get()
    my_label["text"] = user_input


# Button
my_button = Button(text="Click me!", font=FONT, command=button_clicked,
                   fg="orange", bg="#92A8A0")  # Color button fg="blue", bg="green"

# Initialize button
my_button.grid(column=2, row=1)

# Button
new_button = Button(text="Click me!", font=FONT, command=button_clicked,
                   fg="orange", bg="#92A8A0")  # Color button fg="blue", bg="green"

# Initialize button
new_button.grid(column=3, row=0)

# Entry component
input_field = Entry(width=20, font=FONT, fg="white", bg="#92A8A0")

# Initialize input field
input_field.grid(column=4, row=3)




# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

window.mainloop()