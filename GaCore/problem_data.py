# problem_data.py

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

