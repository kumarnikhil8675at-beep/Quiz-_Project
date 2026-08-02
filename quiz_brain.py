import html

class Brain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.current_question = None
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        question = html.unescape(self.current_question.text)
        return f"Q{self.question_number}: {question}"

    def check(self, answer):
        if answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False