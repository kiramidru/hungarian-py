def square_number(x):
    return x**2


def cube_number(x):
    return x**3


def absolute_value(x):
    return abs(x)


def factorial(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def fibonacci(x):
    if x < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a
