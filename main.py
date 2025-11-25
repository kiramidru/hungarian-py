import numpy as np
from scipy.optimize import linear_sum_assignment

# -------------------------------------------------------
# 1. Example cost matrices (execution times)
# Each matrix: rows = test cases, columns = functions
# -------------------------------------------------------

cost_matrix_1 = np.array([
    [0.22, 0.38, 0.95, 0.13, 0.46],
    [0.11, 0.59, 0.63, 0.91, 0.58],
    [0.78, 0.21, 0.40, 0.79, 0.88],
    [0.42, 0.41, 0.16, 0.23, 0.78],
    [0.65, 0.79, 0.36, 0.28, 0.18]
])

cost_matrix_2 = np.array([
    [0.32, 0.28, 0.85, 0.09, 0.54],
    [0.22, 0.49, 0.53, 0.81, 0.68],
    [0.68, 0.31, 0.30, 0.89, 0.78],
    [0.52, 0.31, 0.06, 0.33, 0.68],
    [0.75, 0.69, 0.46, 0.38, 0.28]
])

cost_matrix_3 = np.array([
    [0.28, 0.35, 0.92, 0.16, 0.49],
    [0.18, 0.55, 0.61, 0.86, 0.62],
    [0.74, 0.26, 0.38, 0.83, 0.82],
    [0.45, 0.39, 0.11, 0.27, 0.72],
    [0.69, 0.77, 0.40, 0.32, 0.22]
])

cost_matrices = [cost_matrix_1, cost_matrix_2, cost_matrix_3]

# -------------------------------------------------------
# 2. Compute average cost matrix
# -------------------------------------------------------

avg_cost_matrix = np.mean(cost_matrices, axis=0)
print("Average Cost Matrix:\n", avg_cost_matrix)

# -------------------------------------------------------
# 3. Apply Hungarian algorithm
# -------------------------------------------------------

row_ind, col_ind = linear_sum_assignment(avg_cost_matrix)

# -------------------------------------------------------
# 4. Output results
# -------------------------------------------------------

print("\nOptimal Assignment (Test Case → Function):")
functions = ["square", "cube", "absolute", "factorial", "fibonacci"]

total_cost = 0
for r, c in zip(row_ind, col_ind):
    cost = avg_cost_matrix[r][c]
    total_cost += cost
    print(f"Test Case {r+1} → {functions[c]}, cost = {cost:.6f}")

print(f"\nTotal Optimized Cost: {total_cost:.6f}")

