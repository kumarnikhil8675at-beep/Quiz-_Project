import tkinter
from quiz_brain import brain

THEME_COLOR = "#375362"

class userinterface:
    def __init__(self,quize_brain:brain):
        self.quize=quize_brain 
        
        self.windows=tkinter.Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas=tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=1,row=1,columnspan=2,pady=20)
        self.content=self.canvas.create_text(150,125,width=280,text="hello",font=("Arial",10,"bold"))
        
        self.image=tkinter.PhotoImage(file="./images/true.png")
        self.images=tkinter.PhotoImage(file="./images/false.png")
        
        self.right=tkinter.Button(text="",image=self.image,command=self.checkright)
        self.right.grid(column=1,row=2)
        self.left=tkinter.Button(text="",image=self.images,command=self.checkemain)
        self.left.grid(column=2,row=2)

        self.change_text()
        self.windows.mainloop()
        
    def change_text(self):
        self.canvas.config(bg="white")
        if self.quize.still_has_questions():
            q_text=self.quize.next_question()
            self.canvas.itemconfig(self.content,text=q_text)
        else:
            self.canvas.itemconfig(self.content, text="You've reached the end of the quiz.")
            self.left.config(state="disabled")
            self.right.config(state="disabled")
        
    def checkright(self):
        self.givefeedback(self.quize.check("true"))
        
    def checkemain(self):
        self.givefeedback(self.quize.check("false"))

            
    def givefeedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.change_text)

