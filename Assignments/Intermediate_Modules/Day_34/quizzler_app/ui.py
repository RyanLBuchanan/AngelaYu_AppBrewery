from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 10, "bold")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Create score label
        self.score_label = Label(bg=THEME_COLOR, padx=20, pady=20, text="Score: 0", fg="white", font=SCORE_FONT)
        self.score_label.grid(column=1, row=0)

        # Set up the Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Create question text box
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=QUESTION_FONT,
            fill=THEME_COLOR)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Instantiate QuizBrain for button press
        self.quiz_brain = QuizBrain(question_data)

        # Create the "True" check button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  command=self.true_pressed)

        self.true_button.grid(column=0, row=2)

        # Create the "False" x button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        # Bind the space bar key to the exit_program function
        self.window.bind("<space>", self.exit_program)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    # Function for closing on space bar
    def exit_program(self, event):
        self.window.destroy()  # Destroy the Tk window
