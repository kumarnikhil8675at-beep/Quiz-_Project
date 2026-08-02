from question_model import question
from quiz_brain import brain
import data
from ui import userinterface

user_list=[]

for a in data.question_data:
    questions=question(a["question"],a["correct_answer"])
    user_list.append(questions)
    
answers=brain(user_list)    
userinterface(answers)