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
    total_cost = avg_cost_matrix[row_ind, col_ind].sum()
    return total_cost, row_ind, col_ind


def comparison(avg_cost_matrix):
    linear_cost = linear(avg_cost_matrix)
    hungarian_cost, row_ind, col_ind = hungarian(avg_cost_matrix)
    percentage = (linear_cost - hungarian_cost) / linear_cost * 100

    print(f"Total Unoptimized Cost: {linear_cost:.12f}")
    print(f"Total Optimized Cost: {hungarian_cost:.12f}")
    print(f"total improvement: {percentage}%")

    print("\nOptimal Execution Mapping (test → function):")
    assignment_pairs = []
    for r, c in zip(row_ind, col_ind):
        cost = avg_cost_matrix[r][c]
        assignment_pairs.append((r, c, cost))
        print(f"  Test {r} → Function {c}  (cost={cost:.12f})")

    prioritized = sorted(assignment_pairs, key=lambda x: x[2], reverse=True)

    print("\nPrioritized Test Order (descending cost):")
    for t, f, cost in prioritized:
        print(f"  Test {t}: Function {f}, Cost={cost:.12f}")
    return linear_cost, hungarian_cost
