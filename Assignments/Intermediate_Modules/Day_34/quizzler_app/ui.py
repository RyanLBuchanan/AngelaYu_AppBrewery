from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")


        self.window.mainloop()


        # Function for closing on space bar
        def exit_program(event):
            self.window.destroy()  # Destroy the Tk window

        # Bind the space bar key to the exit_program function
        self.window.bind("<space>", exit_program)

        self.window.mainloop()
