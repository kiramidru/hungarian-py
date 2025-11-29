from matrix import average_matrix
from load import load_requirements, load_test_cases
from prioritization import comparison

test_cases = load_test_cases()
functions = load_requirements()

avg_cost_matrix = average_matrix(functions, test_cases)
comparison(avg_cost_matrix)
