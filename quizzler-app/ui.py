from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.right = PhotoImage(file="./images/true.png")
        self.wrong = PhotoImage(file="./images/false.png")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=FONT, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question = self.canvas.create_text(150, 125,width=280, text="question", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.right_button = Button(image=self.right, pady=20, highlightthickness=0, command=self.check_if_true)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=self.wrong, pady=20, highlightthickness=0, command=self.check_if_false)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_if_true(self):
        right_answer = self.quiz.check_answer("False")
        self.check_if_right(right_answer)

    def check_if_false(self):
        right_answer = self.quiz.check_answer("False")
        self.check_if_right(right_answer)

    def check_if_right(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)
