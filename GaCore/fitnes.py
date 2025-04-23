# fitness.py

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


def fitness(individual):
    node_loads = [{"cpu": 0, "memory": 0, "bandwidth": 0, "time": 0} for _ in nodes]
    penalty = 0
    
    # Calcular cargas y penalizaciones
    for task_idx, node_idx in enumerate(individual):
        task = tasks[task_idx]
        node = nodes[node_idx]
        load = node_loads[node_idx]
        
        load["cpu"] += task["cpu"]
        load["memory"] += task["memory"]
        load["bandwidth"] += task["bandwidth"]
        load["time"] += task["times"][node_idx]
        
        # Penalización proporcional al exceso
        cpu_usage = load["cpu"] / (node["cpu"] * constraints["cpu"])
        mem_usage = load["memory"] / (node["memory"] * constraints["memory"])
        bw_usage = load["bandwidth"] / (node["bandwidth"] * constraints["bandwidth"])
        
        penalty += max(0, cpu_usage - 1) + max(0, mem_usage - 1) + max(0, bw_usage - 1)
    
    # Componentes del fitness
    makespan = max(load["time"] for load in node_loads)
    max_possible_time = sum(max(task["times"]) for task in tasks)
    
    utilization = sum(
        min(1, load["cpu"]/(node["cpu"]*constraints["cpu"])) * 0.4 +
        min(1, load["memory"]/(node["memory"]*constraints["memory"])) * 0.4 +
        min(1, load["bandwidth"]/(node["bandwidth"]*constraints["bandwidth"])) * 0.2
        for load, node in zip(node_loads, nodes)
    ) / len(nodes)
    
    # Fitness combinado
    fitness_value = (0.5 * (1 - makespan/max_possible_time) + 
                    0.3 * utilization + 
                    0.2 * (1 - min(1, penalty/len(tasks)))) * 100
    
    return fitness_value