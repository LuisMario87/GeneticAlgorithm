from ga_core.algoritmoGen import genetic_algorithm
from ga_core.utils import plot_fitness
if __name__ == "__main__":
    best_solution, history = genetic_algorithm()
    print("Mejor solución encontrada:")
    print(best_solution)
    print(plot_fitness(history))
