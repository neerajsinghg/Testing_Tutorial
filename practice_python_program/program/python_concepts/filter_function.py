"""
`filter()` Function Usage
Interview Question: How does `filter()` work?
Explanation: `filter(predicate, iterable)` yields items from `iterable` where `predicate(item)` evaluates to True.
"""

def filter_evens(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print("Original:", numbers)
    print("Filtered Evens:", filter_evens(numbers))
