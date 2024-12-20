from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_NAME = "Courier"
CARD = ""
FALSE = "day 34/images/false.png"
TRUE = "day 34/images/true.png"
class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.minsize(width=250, height=250)
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)      
        
        self.score = 0
        self.score_label = Label(pady=15, text=f"Score: {self.score}", font=(FONT_NAME, 15), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=250, height=250, bg="white",)
        self.question_label = self.canvas.create_text(
            125, 125, 
            width=230,
            text="Questions", 
            fill=THEME_COLOR,
            font=(FONT_NAME, 15) )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)
        #self.question_label.grid(row=1, column=0, columnspan=2)
        self.true_image = PhotoImage(file=TRUE)
        #self.canvas.create_image(150, 207, image = self.true_image)
        self.true_button=Button(image=self.true_image, highlightthickness=0, command=self.right_pressed, padx=20, pady=20)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)
        
        self.false_image = PhotoImage(file=FALSE)
        #self.canvas.create_image(150, 207, image=self.false_image)
        self.false_button=Button(image=self.false_image, highlightthickness=0, command=self.false_pressed, padx=20, pady=20)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else: 
            self.canvas.itemconfig(self.question_label, text=f"There is no more questions left. Your score is {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def right_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right=is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right=is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config( bg="green")
            
        else: 
            self.canvas.config( bg="red")
        self.window.after(1000, self.get_next_question)