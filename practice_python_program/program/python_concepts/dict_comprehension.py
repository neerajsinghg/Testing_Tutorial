"""
Dictionary Comprehension Syntax
Interview Question: How do you create dictionaries using dictionary comprehension?
Explanation: Syntax `{key_expr: val_expr for item in iterable}` builds dictionary mappings succinctly.
"""

def map_number_to_square(numbers: list[int]) -> dict[int, int]:
    return {x: x ** 2 for x in numbers}

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print("Dict Comprehension Output:", map_number_to_square(numbers))
