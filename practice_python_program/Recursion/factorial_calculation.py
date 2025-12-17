# 1. Factorial Calculation
# This classic example calculates the factorial of a non-negative integer. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")