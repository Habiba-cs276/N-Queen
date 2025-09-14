import random

def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def heuristic(board):
    h = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def get_best_neighbor(board):
    n = len(board)
    best = board[:]
    best_h = heuristic(board)
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                new_board = board[:]
                new_board[col] = row
                h = heuristic(new_board)
                if h < best_h:
                    best = new_board
                    best_h = h
    return best, best_h

def hill_climbing(n):
    for _ in range(50):  # 50 tries
        board = random_board(n)
        h = heuristic(board)
        while h > 0:
            next_board, next_h = get_best_neighbor(board)
            if next_h >= h:
                break
            board = next_board
            h = next_h
        if h == 0:
            return board
    return None
