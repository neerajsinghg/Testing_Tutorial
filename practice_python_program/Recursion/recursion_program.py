# Recursion in Python is a programming technique where a function calls itself to solve a complex problem by breaking it into smaller, manageable parts. 
# Every recursive function must have a base case (stopping condition) and a recursive case (calls itself with a smaller input). 
# Here are several common Python programs that use recursion:

# 1. Factorial Calculation
# This classic example calculates the factorial of a non-negative integer. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")
 
# 2. Fibonacci Sequence
# This program generates the nth number in the Fibonacci sequence. 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nth_term = 7
print(f"The {nth_term}th Fibonacci number is {fibonacci(nth_term)}")
 
# 3. Sum of Natural Numbers
# This function calculates the sum of all natural numbers up to a given number n. 

def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

num = 4
print(f"The sum of natural numbers up to {num} is {sum_natural_numbers(num)}")
 
# 4. Reversing a String
# A recursive approach to reverse a string character by character. 

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

my_string = "hello"
print(f"The reversed string of '{my_string}' is '{reverse_string(my_string)}'")

# 5. Traversing a Nested List
# Recursion is ideal for working with nested data structures like lists within lists. 
def sum_nested_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

my_list = [1, 2, [3, 4], [5, 6, [7, 8]]]
print(f"The sum of the nested list is: {sum_nested_list(my_list)}")
 