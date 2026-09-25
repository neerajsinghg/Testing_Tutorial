"""
`map()` Function Usage
Interview Question: What is `map()` and how does it transform iterables?
Explanation: `map(func, iterable)` applies function `func` to every item of `iterable` yielding an iterator.
"""

def double_elements(numbers: list[int]) -> list[int]:
    return list(map(lambda x: x * 2, numbers))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print("Original:", numbers)
    print("Mapped (Doubled):", double_elements(numbers))
