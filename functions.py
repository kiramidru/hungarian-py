def square(x):
    return x * x


def cube(x):
    return x * x * x


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result
