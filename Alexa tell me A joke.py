import tkinter as tk
from tkinter import messagebox
import random

class JokeTelling:
    def __init__(self, root, joke_file="randomJokes.txt"):
        self.root = root
        self.root.title("Joke Teller")
        self.root.geometry("400x400")
        
        # jokes from file
        self.jokes = []
        self.load_jokes_from_file(joke_file)
        
        self.current_joke = ""
        self.setup = ""
        self.punchline = ""
        
        self.create_widgets()
    
    def load_jokes_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Read all lines and remove empty lines
                self.jokes = [line.strip() for line in file if line.strip()]
            
            if not self.jokes:
                self.jokes = ["No jokes found in the file!"]
                messagebox.showwarning("Warning", "The joke file is empty!")
            else:
                print(f"Successfully loaded {len(self.jokes)} jokes from {filename}")
                
        except FileNotFoundError:
            error_msg = f"Joke file '{filename}' not found!\nPlease make sure the file exists in the same folder."
            messagebox.showerror("File Error", error_msg)
            self.jokes = ["Joke file not found! Please check the file."]
        except Exception as e:
            error_msg = f"Error reading joke file: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.jokes = ["Error loading jokes from file."]
    
    def create_widgets(self):
        # Status label to show how many jokes loaded
        self.status_label = tk.Label(self.root, text=f"Loaded {len(self.jokes)} jokes", 
                                   font=("Arial", 8), fg="blue")
        self.status_label.pack(pady=5)
        
        # Tell a joke button
        self.joke_btn = tk.Button(self.root, text="Tell a Joke", 
                                 command=self.tell_joke, font=("Arial", 12),
                                 bg="lightyellow", width=15)
        self.joke_btn.pack(pady=20)
        
        # Joke display
        self.setup_label = tk.Label(self.root, text="", font=("Arial", 10), 
                                   wraplength=350, justify="center")
        self.setup_label.pack(pady=5)
        
        self.punchline_label = tk.Label(self.root, text="", font=("Arial", 10, "bold"),
                                       fg="red", wraplength=350, justify="center")
        self.punchline_label.pack(pady=5)
        
        # Control buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        self.show_btn = tk.Button(btn_frame, text="Show Punchline", 
                                 command=self.show_punchline, state="disabled")
        self.show_btn.pack(side="left", padx=7)
        
        self.next_btn = tk.Button(btn_frame, text="Next Joke", 
                                 command=self.next_joke, state="disabled")
        self.next_btn.pack(side="left", padx=7)
        
        tk.Button(btn_frame, text="Exit", command=self.root.quit).pack(side="left", padx=7)
    
    def tell_joke(self):
        if self.jokes:
            self.current_joke = random.choice(self.jokes)
            
            # Split joke into setup and punchline
            if '?' in self.current_joke:
                parts = self.current_joke.split('?', 1)
                self.setup = parts[0] + "?"
                self.punchline = parts[1].strip()
            elif ':' in self.current_joke:
                parts = self.current_joke.split(':', 1)
                self.setup = parts[0] + ":"
                self.punchline = parts[1].strip()
            else:
                # If no clear separator, try to split at common patterns
                if ' - ' in self.current_joke:
                    parts = self.current_joke.split(' - ', 1)
                    self.setup = parts[0]
                    self.punchline = parts[1].strip()
                else:
                    # If still no separator, use the whole joke
                    self.setup = self.current_joke
                    self.punchline = "😂"
            
            self.setup_label.config(text=self.setup)
            self.punchline_label.config(text="")
            
            self.joke_btn.config(state="disabled")
            self.show_btn.config(state="normal")
            self.next_btn.config(state="normal")
        else:
            messagebox.showwarning("No Jokes", "No jokes available to tell!")
    
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
    app = JokeTelling(root, "randomJokes.txt")
    root.mainloop()