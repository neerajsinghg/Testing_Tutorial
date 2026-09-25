"""
18. Find Duplicate Number in a List
Interview Note: Uses a hash set to track seen elements in O(1) average lookup time.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_duplicate(numbers: list) -> int | None:
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    print("Input:", numbers)
    print("Duplicate:", find_duplicate(numbers))
