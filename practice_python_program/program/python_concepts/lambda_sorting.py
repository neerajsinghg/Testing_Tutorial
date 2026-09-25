"""
Lambda Functions with sorted()
Interview Question: How do you use anonymous lambda functions for custom sorting?
Explanation: Lambda functions `lambda x: expression` provide inline key functions for sorting sequences.
"""

def sort_with_lambda(numbers: list[int]) -> list[int]:
    return sorted(numbers, key=lambda x: x)

if __name__ == "__main__":
    numbers = [5, 2, 8, 1]
    print("Original:", numbers)
    print("Lambda Sorted:", sort_with_lambda(numbers))
