from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizinterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, text="param", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        false_img_raw = Image.open(r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\quizzler-app-start\images\false.png")
        false_img_resized = false_img_raw.resize((100, 100))
        self.false_img = ImageTk.PhotoImage(false_img_resized)
        
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)  
        self.false_button.grid(column=1, row=2)
        
        true_img_raw = Image.open(r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\quizzler-app-start\images\true.png")
        true_img_resized = true_img_raw.resize((100, 100))
        self.true_img = ImageTk.PhotoImage(true_img_resized)
        
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        
        self.next_question()
        
        self.window.mainloop()
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(self.question_text, text="you've reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
            
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)