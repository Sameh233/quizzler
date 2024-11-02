from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class QuizInterface:
    
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)
        
        self.score_label = Label(text= "Score: 0", bg= THEME_COLOR, fg= "white", font= ("Arial", 10, "bold"))
        self.score_label.grid(row= 0, column= 1)
        
        self.canvas = Canvas(width= 300, height= 250, highlightthickness= 0, bg= "white")
        self.question = self.canvas.create_text(150,125,text="", font= FONT,width= 280 ,fill= THEME_COLOR)
        
        self.canvas.grid(row=1, column=0, columnspan= 2, pady= 50)
        
        cross_mark = PhotoImage(file="images/false.png")
        self.false_button = Button(image= cross_mark, highlightthickness= 0, command= self.false_guess)
        self.false_button.grid(row=2, column= 1)
        
        check_mark = PhotoImage(file="images/true.png")
        self.true_button = Button(image= check_mark, highlightthickness= 0, command= self.true_guess)
        self.true_button.grid(row=2, column= 0)
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg= "white") 
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions() :
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text = "You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state= "disabled")
            messagebox.showinfo("Score", f"Your final score is: {self.quiz.score}/{self.quiz.question_number}." )
        
    def true_guess(self):
       self.give_feedback(self.quiz.check_answer("True"))
        
    def false_guess(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    
    def give_feedback(self, is_right):
        if is_right : 
            self.canvas.config(bg= "green")
        else: 
            self.canvas.config(bg= "red") 
            
        self.window.after(1000, self.get_next_question)
        
        
        
    
        
        

