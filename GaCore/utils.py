# utils.py

import matplotlib.pyplot as plt

def plot_fitness(history):
    plt.plot(history)
    plt.title("Evolución del Fitness")
    plt.xlabel("Generaciones")
    plt.ylabel("Fitness")
    plt.grid()
    plt.show()
