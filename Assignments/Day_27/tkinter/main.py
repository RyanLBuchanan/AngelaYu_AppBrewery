from tkinter import *
from turtle import bgcolor

FONT = ("Press Start 2P", 12, "normal")


# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


window = Tk()
window.title("Hello GUI")
window.minsize(width=900, height=700)
window.configure(bg="#1F3B4D")

# Label
my_label = Label(text="I am a label.", font=FONT, fg="orange", bg="#92A8A0")

# Initialize
my_label.pack()  # Alignment with "side="left"

# Change label text
my_label["text"] = "New text"


# my_label.config(text="Newer text", fg="green", bg="gray")

# Button click function
def button_clicked():
    user_input = input_field.get()
    my_label["text"] = user_input


# Button
my_button = Button(text="Click me!", font=FONT, command=button_clicked,
                   fg="orange", bg="#92A8A0")  # Color button fg="blue", bg="green"

# Initialize button
my_button.pack()

# Entry component
input_field = Entry(width=20, font=FONT, fg="white", bg="#92A8A0")

# Initialize input field
input_field.pack()

# Instantiates textbox
text_box = Text(height=5, width=30, font=FONT, fg="#12232E", bg="#92A8A0")

# Adds cursor in textbox
text_box.focus()

# Adds placeholder text in textbox
text_box.insert(END, "Type your input here . . .")

# Get the current value in textbox at line 1, character 0
print(text_box.get("1.0", END))
# Initialize textbox
text_box.pack()


# Create spinbox function
def spinbox_used():
    # Get the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, font=FONT, fg="#12232E", bg="#92A8A0", command=spinbox_used)

# Initialize spinbox
spinbox.pack()

# Scale function; called with current value
def scale_used(value):
    print(value)


# Instantiate scale
scale = Scale(from_=0, to=100, font=FONT, fg="#12232E", bg="#92A8A0", command=scale_used)

# Initialize scale
scale.pack()

def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# Variable to hold the checked state, 0 if off, 1 is on
checked_state = IntVar()

# Instantiate checkbutton
checkbutton = Checkbutton(text="Is On?", font=FONT, fg="#12232E", bg="#92A8A0",
                          variable=checked_state, command=checkbutton_used)

# Get check button state
checked_state.get()

# Initialize check button
checkbutton.pack()

# Radio button function
def radio_used():
    print(radio_state.get())


# Variable to hold the radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(font=FONT, fg="cyan", bg="#92A8A0", text="T' Pol Vulcanness", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(font=FONT, fg="cyan", bg="#92A8A0", text="Seven of Nine", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(font=FONT, fg="cyan", bg="#92A8A0", text="Nurse Chapel", value=3, variable=radio_state, command=radio_used)

# Initialize radio buttons
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Listbox function
def listbox_used(event):
    # Get the current selection from the listbox
    print(listbox.get(listbox.curselection()))


# Initialize listbox
listbox = Listbox(height=11, width=50, font=FONT, fg="white", bg="#92A8A0")

# Create listbox list
cybergirls = [
    "Seven of Nine: Star Trek: Voyager",
    "T'Pol: Star Trek: Enterprise",
    "Deanna Troi: Star Trek: The Next Generation",
    "Nyota Uhura: Star Trek: The Original Series",
    "Ezri Dax: Star Trek: Deep Space Nine",
    "B'Elanna Torres: Star Trek: Voyager",
    "Jadzia Dax: Star Trek: Deep Space Nine",
    "Christine Chapel: Star Trek: The Original Series",
    "Ro Laren: Star Trek: The Next Generation",
    "Major Motoko Kusanagi (Ghost in the Shell)"
    ]

# Iterate over cybergirls
for girl in cybergirls:
    listbox.insert(END, girl)

listbox.bind("<<ListboxSelect>>", listbox_used)

# Initialize listbox
listbox.pack()

# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

window.mainloop()
