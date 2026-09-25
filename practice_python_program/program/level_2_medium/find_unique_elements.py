"""
21. Find Unique Elements (Elements Appearing Exactly Once)
Interview Note: Uses a frequency map to identify elements with frequency count == 1.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_unique_elements(numbers: list) -> list:
    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1
    return [number for number, value in count.items() if value == 1]

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Input:", numbers)
    print("Unique elements (count == 1):", find_unique_elements(numbers))
