"""
Rotate List Right by K Positions
Interview Note: Uses slicing with modulo operator k % len(numbers) to rotate array in-place or return copy.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def rotate_right(numbers: list, k: int) -> list:
    if not numbers:
        return []
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    k = 2
    print("Rotated right:", rotate_right(numbers, k))
