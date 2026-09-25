"""
34. Rotate a List Right by k Positions
Interview Note: Uses slicing with modulo operator k % len(numbers) to handle shift wrapping.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def rotate_list(numbers: list, k: int) -> list:
    if not numbers:
        return []
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    k = 2
    print("Original:", numbers)
    print(f"Rotated right by {k}:", rotate_list(numbers, k))
