"""
11. Remove Duplicates from a List
Interview Note: Demonstrates set conversion (unordered) and loop method (preserves original insertion order).
Time Complexity: O(n)
Space Complexity: O(n)
"""

def remove_duplicates_unordered(numbers: list) -> list:
    return list(set(numbers))

def remove_duplicates_preserve_order(numbers: list) -> list:
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Unordered (set):", remove_duplicates_unordered(numbers))
    print("Order preserved:", remove_duplicates_preserve_order(numbers))
