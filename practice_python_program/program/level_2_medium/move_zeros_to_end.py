"""
22. Move All Zeros to the End
Interview Note: Filters non-zero elements into a list and appends remaining zeros.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def move_zeros_to_end(numbers: list[int]) -> list[int]:
    result = [number for number in numbers if number != 0]
    result += [0] * (len(numbers) - len(result))
    return result

if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    print("Input:", numbers)
    print("Output:", move_zeros_to_end(numbers))
