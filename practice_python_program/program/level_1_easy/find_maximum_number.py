"""
8. Find Maximum Number in a List
Interview Note: Demonstrates linear scan without built-in max().
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max(numbers: list[int | float]) -> int | float:
    if not numbers:
        raise ValueError("List is empty")
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == "__main__":
    numbers = [10, 25, 7, 90, 45]
    print("Maximum:", find_max(numbers))
