"""
Find Second Smallest Number in a List
Interview Note: Uses sorted(set(numbers))[1] to remove duplicates and find second element.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def find_second_smallest(numbers: list[int | float]) -> int | float:
    unique = sorted(set(numbers))
    if len(unique) < 2:
        raise ValueError("List must contain at least two unique numbers")
    return unique[1]

if __name__ == "__main__":
    numbers = [10, 5, 20, 3, 8]
    print("Numbers:", numbers)
    print("Second Smallest:", find_second_smallest(numbers))
