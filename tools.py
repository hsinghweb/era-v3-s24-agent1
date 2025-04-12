import logging

def log_function(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args} {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def strings_to_chars_to_int(s):
    return [ord(c) for c in s]

import math

@log_function
def int_list_to_exponential_values(lst):
    return [math.e**x for x in lst]



@log_function
def fibonacci_numbers(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

@log_function
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return [1]
    factorials = [1]  # 0!
    current = 1
    for i in range(1, n):
        current *= i
        factorials.append(current)
    return factorials

@log_function
def calculate_sum(lst):
    if not lst:
        return 0
    return sum(lst)

@log_function
def calculate_product(lst):
    if not lst:
        return 0
    result = 1
    for num in lst:
        result *= num
    return result
