import time
import numpy as np


def cost_matrix(functions, test_cases):
    cost_matrix = np.zeros((len(test_cases), len(functions)))

    for i, tc in enumerate(test_cases):
        for j, func in enumerate(functions):
            start = time.perf_counter()
            func(tc)
            end = time.perf_counter()
            cost_matrix[i][j] = end - start
    return cost_matrix


def average_matrix(functions, test_cases, runs=3):
    matrices = []
    for _ in range(runs):
        matrix = cost_matrix(functions, test_cases)
        matrices.append(matrix)

    avg_cost_matrix = np.mean(matrices, axis=0)
    return avg_cost_matrix
