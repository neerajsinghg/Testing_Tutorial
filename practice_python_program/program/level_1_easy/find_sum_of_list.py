"""
10. Find Sum of List Elements
Interview Note: Accumulates values across iterable without built-in sum().
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_sum(numbers: list[int | float]) -> int | float:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("Total Sum:", find_sum(numbers))
