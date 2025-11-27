import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("650x520")
        self.filename = "studentMarks.txt"
        self.students = []

        self.bg_color = "#e7eff6"
        self.button_color = "#4b79a1"
        self.button_text_color = "white"
        self.output_bg = "white"
        self.title_color = "#2c3e50"

        self.root.configure(bg=self.bg_color)

        self.ensure_file()
        self.load_students()
        self.build_ui()

    def ensure_file(self):
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def load_students(self):
        self.students.clear()
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    try:
                        self.students.append({
                            "code": int(parts[0]),
                            "name": parts[1],
                            "coursework": [int(parts[2]), int(parts[3]), int(parts[4])],
                            "exam": int(parts[5])
                        })
                    except:
                        pass

    def save(self):
        with open(self.filename, "w") as file:
            for s in self.students:
                cw = s["coursework"]
                file.write(f"{s['code']},{s['name']},{cw[0]},{cw[1]},{cw[2]},{s['exam']}\n")

    def calc(self, s):
        total = sum(s["coursework"]) + s["exam"]
        percentage = (total / 160) * 100
        grade = "A" if percentage >= 70 else "B" if percentage >= 60 else "C" if percentage >= 50 else "D" if percentage >= 40 else "F"
        return percentage, grade

    def build_ui(self):
        tk.Label(
            self.root,
            text="Student Manager",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.title_color
        ).pack(pady=12)

        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack()

        buttons = [
            ("View All", self.view_all),
            ("Find", self.find_student),
            ("Top", self.top_student),
            ("Lowest", self.lowest_student),
            ("Add", self.add_student),
            ("Delete", self.delete_student),
        ]

        for i, (txt, cmd) in enumerate(buttons):
            tk.Button(
                btn_frame, text=txt, width=10, command=cmd,
                bg=self.button_color, fg=self.button_text_color,
                font=("Arial", 10, "bold")
            ).grid(row=0, column=i, padx=5, pady=5)

        self.output = tk.Text(
            self.root, height=20,
            font=("Consolas", 10),
            bg=self.output_bg,
            fg="#2d3436",
            relief="ridge",
            borderwidth=3
        )
        self.output.pack(padx=10, pady=10, fill="both", expand=True)

        self.view_all()

    def show(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)

    def view_all(self):
        if not self.students:
            self.show("No students found.")
            return

        text = ""
        for s in self.students:
            p, g = self.calc(s)
            text += (f"{s['code']} - {s['name']}\n"
                     f"Coursework: {s['coursework']} | Exam: {s['exam']}\n"
                     f"Percentage: {p:.1f}% | Grade: {g}\n"
                     f"{'-'*45}\n")
        self.show(text)

    def find_student(self):
        code = simpledialog.askinteger("Find Student", "Enter student code:")
        if code is None: return

        for s in self.students:
            if s["code"] == code:
                p, g = self.calc(s)
                self.show(f"Found:\n\n{s['code']} - {s['name']}\nPercentage: {p:.1f}% | Grade: {g}")
                return
        self.show("Student not found!")

    def add_student(self):
        code = simpledialog.askinteger("Code", "Enter student code:")
        name = simpledialog.askstring("Name", "Enter student name:")
        cw1 = simpledialog.askinteger("Coursework 1", "Enter mark:")
        cw2 = simpledialog.askinteger("Coursework 2", "Enter mark:")
        cw3 = simpledialog.askinteger("Coursework 3", "Enter mark:")
        exam = simpledialog.askinteger("Exam", "Enter exam mark:")

        if None in (code, name, cw1, cw2, cw3, exam):
            return messagebox.showwarning("Incomplete", "All fields required!")

        self.students.append({
            "code": code,
            "name": name,
            "coursework": [cw1, cw2, cw3],
            "exam": exam
        })

        self.save()
        self.view_all()

    def delete_student(self):
        code = simpledialog.askinteger("Delete", "Enter student code:")
        if code is None: return

        for s in self.students:
            if s["code"] == code:
                self.students.remove(s)
                self.save()
                self.view_all()
                return
        self.show("Student not found!")

    def top_student(self):
        best = max(self.students, key=lambda s: self.calc(s)[0])
        p, g = self.calc(best)
        self.show(f"Top Student:\n\n{best['name']} ({best['code']})\n{p:.1f}% | Grade {g}")

    def lowest_student(self):
        low = min(self.students, key=lambda s: self.calc(s)[0])
        p, g = self.calc(low)
        self.show(f"Lowest Student:\n\n{low['name']} ({low['code']})\n{p:.1f}% | Grade {g}")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    StudentManager(root)
    root.mainloop()
