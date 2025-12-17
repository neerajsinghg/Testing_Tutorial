# 2. Fibonacci Sequence
# This program generates the nth number in the Fibonacci sequence. 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nth_term = 7
print(f"The {nth_term}th Fibonacci number is {fibonacci(nth_term)}")
 