"""
List Comprehension Syntax
Interview Question: What is list comprehension and why is it preferred?
Explanation: Concise syntax `[expression for item in iterable if condition]` creating lists efficiently in Python C-level loops.
"""

def get_squares(numbers: list[int]) -> list[int]:
    return [x ** 2 for x in numbers]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Original:", numbers)
    print("Squares List Comprehension:", get_squares(numbers))
