import random
from algorithms.hill_climbing import random_board

def fitness(board):
    n = len(board)
    non_attacking = 0
    total_pairs = n * (n - 1) // 2
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking / total_pairs

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 2)
    return p1[:point] + p2[point:]

def mutate(board, rate=0.2):
    if random.random() < rate:
        i = random.randint(0, len(board) - 1)
        board[i] = random.randint(0, len(board) - 1)
    return board

def genetic_algorithm(n):
    population = [random_board(n) for _ in range(200)]
    for _ in range(2000): 
        population.sort(key=lambda b: -fitness(b))
        if fitness(population[0]) == 1.0:
            return population[0]
        new_pop = population[:10]
        while len(new_pop) < 200:
            p1, p2 = random.choices(population[:20], k=2)
            child = mutate(crossover(p1, p2))
            new_pop.append(child)
        population = new_pop
    return None
