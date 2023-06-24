from tkinter import *

FONT = ("Press Start 2P", 16, "normal")

# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


window = Tk()
window.title("Hello GUI")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label.", font=FONT, fg="orange")
my_label.pack()  # Alignment with "side="left"
my_label["text"] = "New text"

# Button click function
def button_clicked():
    my_label["text"] = "I got clicked!"


# Button
my_button = Button(text="Click me!", font=FONT, command=button_clicked, fg="orange")  # Color button fg="blue", bg="green"
my_button.pack()





# my_label.config(text="Newer text", fg="green", bg="gray")

# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

window.mainloop()