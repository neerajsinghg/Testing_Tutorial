"""
Move Zeros to the End of List
Interview Note: Separates non-zero elements and concatenates trailing zeros.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def move_zeros(numbers: list[int]) -> list[int]:
    non_zero = [x for x in numbers if x != 0]
    return non_zero + [0] * (len(numbers) - len(non_zero))

if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    print("Original:", numbers)
    print("Zeros moved:", move_zeros(numbers))
