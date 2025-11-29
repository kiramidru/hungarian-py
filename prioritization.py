from scipy.optimize import linear_sum_assignment


def linear(avg_cost_matrix):
    num_tests, num_funcs = avg_cost_matrix.shape
    total_cost = 0

    for i in range(num_tests):
        func_index = i % num_funcs
        total_cost += avg_cost_matrix[i, func_index]
    return total_cost


def hungarian(avg_cost_matrix):
    row_ind, col_ind = linear_sum_assignment(avg_cost_matrix)
    total_cost = 0
    for r, c in zip(row_ind, col_ind):
        cost = avg_cost_matrix[r][c]
        total_cost += cost
    return total_cost


def comparison(avg_cost_matrix):
    linear_cost = linear(avg_cost_matrix)
    hungarian_cost = hungarian(avg_cost_matrix)

    print(f"\nTotal Unoptimized Cost: {linear_cost:.12f}")
    print(f"\nTotal Optimized Cost: {hungarian_cost:.12f}")

    percentage = (linear_cost - hungarian_cost)/linear_cost * 100
    print(f"total improvement: {percentage} %")
