from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# my_question = Question("Did you know that diarrhea is hereditary? ",
#                        "Ya, it runs in your jeans! Bwaaah!")
# my_question.text = "Did you know that diarrhea is hereditary? "
# print(f"{my_question.text}\n{my_question.answer}")

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
