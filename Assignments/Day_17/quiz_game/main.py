from data import question_data
from question_model import Question

# my_question = Question("Did you know that diarrhea is hereditary? ",
#                        "Ya, it runs in your jeans! Bwaaah!")
# my_question.text = "Did you know that diarrhea is hereditary? "
# print(f"{my_question.text}\n{my_question.answer}")

question_bank = []

for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)
#     print(new_question.text)

# print(len(question_bank))
