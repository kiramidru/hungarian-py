from scipy.optimize import linear_sum_assignment
from sklearn.base import np
from sklearn.cluster import KMeans


def linear(avg_cost_matrix):
    num_tests, num_funcs = avg_cost_matrix.shape
    linear_cost = 0

    for i in range(num_tests):
        func_index = i % num_funcs
        linear_cost += avg_cost_matrix[i, func_index]
    return linear_cost


def hungarian(avg_cost_matrix):
    row_ind, col_ind = linear_sum_assignment(avg_cost_matrix)
    hungarian_cost = avg_cost_matrix[row_ind, col_ind].sum()
    return hungarian_cost


def greedy_select(cost_matrix):
    selected_rows = []
    for i in range(cost_matrix.shape[0]):
        selected_rows.append(i)

    return cost_matrix[selected_rows, :]


def optimized_hungarian(avg_cost_matrix, k=3):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(avg_cost_matrix)

    final_assignments = []
    optimized_cost = 0

    for cluster_id in range(k):
        cluster_indices = np.where(cluster_labels == cluster_id)[0]

        if len(cluster_indices) == 0:
            continue

        cluster_matrix = avg_cost_matrix[cluster_indices]
        greedy_matrix = greedy_select(cluster_matrix)
        row_ind, col_ind = linear_sum_assignment(greedy_matrix)
        cluster_cost = greedy_matrix[row_ind, col_ind].sum()

        optimized_cost += cluster_cost

        for r, c in zip(row_ind, col_ind):
            real_test_index = cluster_indices[r]
            final_assignments.append((real_test_index, c, greedy_matrix[r][c]))

    return optimized_cost


def comparison(avg_cost_matrix):
    linear_cost = linear(avg_cost_matrix)
    hungarian_cost = hungarian(avg_cost_matrix)
    optimized_cost = optimized_hungarian(avg_cost_matrix, k=3)

    improvement_1 = (linear_cost - hungarian_cost) / linear_cost * 100
    improvement_2 = (hungarian_cost - optimized_cost) / hungarian_cost * 100

    print(f"Total Unoptimized Cost: {linear_cost:.12f}")
    print(f"Total Optimized Cost: {hungarian_cost:.12f}")
    print(f"Total Optimized Cost (Cluster + Greedy): {optimized_cost:.12f}")

    print(f"\nImprovement (Linear → Hungarian): {improvement_1:.3f}%")
    print(f"Improvement (Hungarian → Optimized Hungarian): {improvement_2:.3f}%")

    return linear_cost, hungarian_cost, optimized_cost
