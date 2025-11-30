from matrix import average_matrix
from load import load_requirements, load_test_cases
from prioritization import comparison
from visualization import plot_comparison

test_cases = load_test_cases()
functions = load_requirements()

avg_cost_matrix = average_matrix(functions, test_cases)
linear_cost, hungarian_cost = comparison(avg_cost_matrix)
plot_comparison(linear_cost, hungarian_cost)
