from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# my_question = Question("Did you know that diarrhea is hereditary? ",
#                        "Ya, it runs in your jeans! Bwaaah!")
# my_question.text = "Did you know that diarrhea is hereditary? "
# print(f"{my_question.text}\n{my_question.answer}")

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# If quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYou're final score: "
      f"{quiz.score}/{quiz.question_number} = "
      f"{round(quiz.score/quiz.question_number * 100)}%.")
