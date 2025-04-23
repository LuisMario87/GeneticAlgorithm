# genetic_algorithm.py

import random
from ga_core.fitnes import fitness
nodes = [
    {"cpu": 8, "memory": 16, "bandwidth": 100},
    {"cpu": 4, "memory": 32, "bandwidth": 50},
    {"cpu": 16, "memory": 8, "bandwidth": 200},
    {"cpu": 12, "memory": 24, "bandwidth": 150},
    {"cpu": 6, "memory": 12, "bandwidth": 80},
]

constraints = {
    "cpu": 0.8,
    "memory": 0.9,
    "bandwidth": 0.75
}

tasks = [
    {"cpu": 2, "memory": 4, "bandwidth": 30, "times": [10, 15, 8, 12, 11]},
    {"cpu": 4, "memory": 8, "bandwidth": 20, "times": [12, 20, 10, 11, 14]},
    {"cpu": 1, "memory": 2, "bandwidth": 10, "times": [8, 10, 6, 7, 9]},
    {"cpu": 3, "memory": 6, "bandwidth": 25, "times": [11, 16, 9, 10, 12]},
    {"cpu": 2, "memory": 10, "bandwidth": 15, "times": [14, 18, 11, 13, 16]},
    {"cpu": 6, "memory": 12, "bandwidth": 40, "times": [20, 25, 15, 17, 22]},
    {"cpu": 1, "memory": 3, "bandwidth": 5, "times": [6, 8, 5, 6, 7]},
    {"cpu": 5, "memory": 14, "bandwidth": 35, "times": [18, 22, 14, 16, 19]},
    {"cpu": 2, "memory": 5, "bandwidth": 10, "times": [9, 12, 7, 8, 10]},
    {"cpu": 3, "memory": 7, "bandwidth": 20, "times": [13, 17, 10, 11, 13]},
]





def create_individual():
    return [random.randint(0, len(nodes)-1) for _ in tasks]

def init_population(size):
    return [create_individual() for _ in range(size)]

def selection(population):
    return max(random.sample(population, 3), key=fitness)

def crossover(p1, p2):
    point = random.randint(1, len(tasks)-2)
    return p1[:point] + p2[point:]

def mutate(individual, rate=0.1):
    for i in range(len(individual)):
        if random.random() < rate:
            individual[i] = random.randint(0, len(nodes)-1)
    return individual

def genetic_algorithm(generations=500, pop_size=50):
    population = init_population(pop_size)
    best = max(population, key=fitness)
    history = []

    for gen in range(generations):
        new_population = []

        for _ in range(pop_size):
            p1 = selection(population)
            p2 = selection(population)
            child = mutate(crossover(p1, p2))
            new_population.append(child)

        population = new_population
        current_best = max(population, key=fitness)
        if fitness(current_best) > fitness(best):
            best = current_best

        history.append(fitness(best))
        print(f"Generación {gen}: Mejor fitness = {fitness(best)}")

    return best, history
