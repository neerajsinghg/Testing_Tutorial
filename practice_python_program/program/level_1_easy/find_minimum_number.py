"""
9. Find Minimum Number in a List
Interview Note: Demonstrates linear scan without built-in min().
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_min(numbers: list[int | float]) -> int | float:
    if not numbers:
        raise ValueError("List is empty")
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == "__main__":
    numbers = [10, 25, 7, 90, 45]
    print("Minimum:", find_min(numbers))
