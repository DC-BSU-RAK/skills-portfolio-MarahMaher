import tkinter as tk
from tkinter import messagebox
import random

class ArithmeticQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Solving")
        self.root.geometry("400x400")
        
        self.score = 0
        self.question_num = 0
        self.first_try = True
        
        self.show_menu()
    
    def show_menu(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Math Solving", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Choose Difficulty:").pack()
        
        tk.Button(self.root, text="Easy", command=lambda: self.start_game("easy")).pack(pady=5)
        tk.Button(self.root, text="Medium", command=lambda: self.start_game("medium")).pack(pady=5)
        tk.Button(self.root, text="Hard", command=lambda: self.start_game("hard")).pack(pady=5)
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def start_game(self, level):
        self.level = level
        self.score = 0
        self.question_num = 0
        self.next_question()
    
    def next_question(self):
        self.question_num += 1
        self.first_try = True
        
        if self.question_num > 10:
            self.show_results()
            return
        
        self.clear_screen()
        
        # Progress
        tk.Label(self.root, text=f"Question {self.question_num}/10 - Score: {self.score}").pack(pady=10)
        
        # Make math problem
        if self.level == "easy":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
        elif self.level == "medium":
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
        else:
            num1 = random.randint(1000, 9999)
            num2 = random.randint(1000, 9999)
        
        # Choose + or -
        if random.random() > 0.5:
            operation = "+"
            answer = num1 + num2
        else:
            operation = "-"
            # Make sure answer is not negative
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        
        self.correct_answer = answer
        
        # Show problem
        tk.Label(self.root, text=f"{num1} {operation} {num2} =", font=("Arial", 18)).pack(pady=20)
        
        self.answer_entry = tk.Entry(self.root, width=10)
        self.answer_entry.pack(pady=10)
        self.answer_entry.focus()
        
        tk.Button(self.root, text="Submit", command=self.check_answer).pack()
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            
            if user_answer == self.correct_answer:
                if self.first_try:
                    self.score += 10
                    messagebox.showinfo("Correct", "Good! +10 points")
                else:
                    self.score += 5
                    messagebox.showinfo("Correct", "Nice! +5 points")
                self.next_question()
            else:
                if self.first_try:
                    self.first_try = False
                    messagebox.showwarning("Wrong", "Try one more time!")
                    self.answer_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Wrong", f"Answer was {self.correct_answer}")
                    self.next_question()
                    
        except:
            messagebox.showerror("Error", "Please enter a number")
    
    def show_results(self):
        self.clear_screen()
        
        tk.Label(self.root, text=f"Final Score: {self.score}/100", font=("Arial", 14)).pack(pady=20)
        
        # Simple grading
        if self.score >= 90:
            grade = "A+"
        elif self.score >= 80:
            grade = "A" 
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "Need Practice"
        
        tk.Label(self.root, text=f"Grade: {grade}").pack(pady=10)
        
        tk.Button(self.root, text="Play Again", command=self.show_menu).pack(pady=5)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack()

# Start the program
root = tk.Tk()
app = ArithmeticQuiz(root)
root.mainloop()