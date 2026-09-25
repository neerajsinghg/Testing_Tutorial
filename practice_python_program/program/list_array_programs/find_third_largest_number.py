"""
Find Third Largest Number in a List
Interview Note: Uses sorted(set(numbers), reverse=True)[2] to get third largest unique value.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def find_third_largest(numbers: list[int | float]) -> int | float:
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 3:
        raise ValueError("List must contain at least three unique numbers")
    return unique[2]

if __name__ == "__main__":
    numbers = [10, 50, 20, 90, 70, 80]
    print("Numbers:", numbers)
    print("Third Largest:", find_third_largest(numbers))
