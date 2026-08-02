from question_model import Question
from quiz_brain import Brain
from ui import UserInterface
import data

question_bank = []

for question in data.question_data:
    new_question = Question(
        question["question"],
        question["correct_answer"]
    )
    question_bank.append(new_question)

quiz = Brain(question_bank)
ui = UserInterface(quiz)