import tkinter as tk
from tkinter import messagebox
import random

class JokeTellingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke Teller")
        self.root.geometry("400x400")
        
        # Simple jokes database
        self.jokes = [
          "What animal can jump higher than a house?Any animal, houses can't jump!",
          "Why did the kid bring a ladder to school?He wanted to go to high school!",
          "What has ears but cannot hear?A cornfield!",
          "Why did the cookie go to the doctor?Because it felt crummy!",
          "What do you call a bear with no teeth?A gummy bear!"
        ]
        
        self.current_joke = ""
        self.setup = ""
        self.punchline = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        # asking alexa to tell a joke
        self.joke_btn = tk.Button(self.root, text="Tell a Joke", 
                                 command=self.tell_joke, font=("Arial", 12),
                                 bg="lightyellow", width=15)
        self.joke_btn.pack(pady=20)
        
        # Joke 
        self.setup_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.setup_label.pack(pady=5)
        
        self.punchline_label = tk.Label(self.root, text="", font=("Arial", 10, "bold"),
                                       fg="red")
        self.punchline_label.pack(pady=5)
        
        # Control buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        self.show_btn = tk.Button(btn_frame, text="Show Answer", 
                                 command=self.show_punchline, state="disabled")
        self.show_btn.pack(side="left", padx=7)
        
        self.next_btn = tk.Button(btn_frame, text="Next ", 
                                 command=self.next_joke, state="disabled")
        self.next_btn.pack(side="left", padx=7)
        
        tk.Button(btn_frame, text="Leave", command=self.root.quit).pack(side="left", padx=7)
    
    def tell_joke(self):
        if self.jokes:
            self.current_joke = random.choice(self.jokes)
            
            if '?' in self.current_joke:
                parts = self.current_joke.split('?', 1)
                self.setup = parts[0] + "?"
                self.punchline = parts[1]
            else:
                self.setup = self.current_joke
                self.punchline = "No punchline"
            
            self.setup_label.config(text=self.setup)
            self.punchline_label.config(text="")
            
            self.joke_btn.config(state="disabled")
            self.show_btn.config(state="normal")
            self.next_btn.config(state="normal")
    
    def show_punchline(self):
        self.punchline_label.config(text=self.punchline)
        self.show_btn.config(state="disabled")
    
    def next_joke(self):
        self.setup_label.config(text="")
        self.punchline_label.config(text="")
        self.joke_btn.config(state="normal")
        self.show_btn.config(state="disabled")
        self.next_btn.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeTellingAssistant(root)
    root.mainloop()