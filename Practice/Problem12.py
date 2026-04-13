import math

n = 5
print(f"The factorial of {n} is {math.factorial(n)}")

def factorial_iterative(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120
