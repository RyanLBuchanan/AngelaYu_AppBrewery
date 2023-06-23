import tkinter as tk
FONT = ("Press Start 2P", 24, "normal")
def exit_program(event):
    window.destroy()  # Destroy the Tk window


window = tk.Tk()
window.title("Hello GUI")
window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="I am a label.", font=FONT, fg="orange")
my_label.pack(side="left")

# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

window.mainloop()