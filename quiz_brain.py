import html

class brain:
    def __init__(self,list):
        self.question_list=list
        self.current_question=None
        self.count=0
        self.intration=0
    
    def still_has_questions(self):
            return self.count < len(self.question_list)
        
    def next_question(self):
        self.current_question=self.question_list[self.count]
        self.count +=1
        question=html.unescape(self.current_question.text)
        return f"Q{self.count}: {question}"
        # self.check()
    
    def check(self,answer):
        if(answer.lower()==self.current_question.answer.lower()):
            # print("Your Answer is Correct")
            self.intration+=1
            return True
        else:
            return False
            # print("Your Answer is Wrong")
        # print(f"correct answer is {self.current_question.answer}")
        # print("scor",self.intration,"/",len(self.question_list))
        # self.next_question()