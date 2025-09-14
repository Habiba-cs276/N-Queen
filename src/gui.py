import tkinter as tk
from tkinter import messagebox
from algorithms.hill_climbing import hill_climbing
from algorithms.genetic import genetic_algorithm

class NQueensApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens")

        tk.Label(root, text="Number of Queens:").pack()
        self.n_entry = tk.Entry(root)
        self.n_entry.pack()

        tk.Label(root, text="Choose the method:").pack()
        self.method = tk.StringVar(value="hill")
        tk.OptionMenu(root, self.method, "hill", "genetic").pack()

        tk.Button(root, text="Start", command=self.solve).pack(pady=5)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

    def draw_board(self, board):
        self.canvas.delete("all")
        n = len(board)
        size = 400 // n
        for i in range(n):
            for j in range(n):
                x1, y1 = j * size, i * size
                x2, y2 = x1 + size, y1 + size
                color = "#EEE" if (i + j) % 2 == 0 else "#333"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                if board[j] == i:
                    self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="red")

    def solve(self):
        try:
            n = int(self.n_entry.get())
            if n < 4:
                messagebox.showerror("Error", "Number must be 4 or more.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        method = self.method.get()
        if method == "hill":
            result = hill_climbing(n)
        else:
            result = genetic_algorithm(n)

        if result:
            self.draw_board(result)
        else:
            messagebox.showinfo("No Solution", "Couldn't find a solution, try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensApp(root)
    root.mainloop()
