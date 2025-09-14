# N-Queen
The N-Queens problem is a classic puzzle in computer science. The objective is to place N chess queens on an N x N chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

# Features
- Solve N-Queens: Find a solution to the N-Queens problem for a given board size (N).

- Two Solving Methods: Choose between two AI algorithms:

   1- Hill Climbing: A local search algorithm that iteratively moves towards a "better" solution by making small changes to the current one.

   2- Genetic Algorithm: A search heuristic inspired by the process of natural selection. It uses concepts like mutation, crossover, and fitness to evolve a population of solutions.

- Interactive GUI: Enter the desired number of queens and select a solving method. The solution is displayed on a visual chessboard.

- Error Handling: The application includes basic validation to ensure the input is a valid number and greater than or equal to 4, as there is no solution for N < 4.

#  How to Run
- Prerequisites: Make sure you have Python 3 installed on your system.

- Dependencies: The project uses the standard tkinter library, which is typically included with Python. No additional installation is required.

- Run the script: Save the provided code as a Python file (e.g., n_queens.py) and run it from your terminal: 
       Bash
       python n_queens.py

#  Project Structure and Algorithms
The code is structured into a few main sections:

1. Helper Functions

- random_board(n): Generates a random initial board configuration of size N x N.

- heuristic(board): Calculates the heuristic value (or number of conflicting queen pairs) for a given board. A heuristic value of 0 indicates a valid solution. This is used    by the Hill Climbing algorithm.

- fitness(board): Calculates the fitness of a board, representing how close it is to a solution. This is used by the Genetic Algorithm. A fitness value of 1.0 indicates a perfect solution.

- crossover(p1, p2): Combines two "parent" boards to create a new "child" board.

- mutate(board): Randomly changes a queen's position on the board to introduce genetic diversity.

2. Solving Algorithms:

- hill_climbing(n): Implements the hill climbing algorithm. It starts with a random board and repeatedly moves to a neighboring board with a lower heuristic value until it reaches a local minimum (or a solution).

- genetic_algorithm(n): Implements the genetic algorithm. It maintains a population of boards, selects the fittest ones for reproduction, and uses crossover and mutation to create a new generation, eventually converging on a solution.

3. GUI Class:
   
 - NQueensApp: This class manages the GUI.

     - __init__: Sets up the main window, input fields, buttons, and the canvas for drawing the board.

     - draw_board: Renders the board and the queen positions on the canvas.

     - solve: The main function that gets the user input, calls the selected solving algorithm, and displays the result.
       
