import tkinter
from quiz_brain import Brain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: Brain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score=tkinter.Label(text="score :",font=("Arial",10,"bold"),bg=THEME_COLOR,fg="white")
        self.score.grid(column=2, row=1)
        
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20)

        self.content = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello",
            font=("Arial", 10, "bold"),
        )

        self.true_image = tkinter.PhotoImage(file="./images/true.png")
        self.false_image = tkinter.PhotoImage(file="./images/false.png")

        self.true_button = tkinter.Button(
            image=self.true_image,
            command=self.check_true,
        )
        self.true_button.grid(column=1, row=3)

        self.false_button = tkinter.Button(
            image=self.false_image,
            command=self.check_false,
        )
        self.false_button.grid(column=2, row=3)

        self.change_text()

        self.window.mainloop()

    def change_text(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.content, text=q_text)
        else:
            self.canvas.itemconfig(
                self.content,
                text="You've reached the end of the quiz.",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.change_text)