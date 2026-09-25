"""
Maximum Subarray Sum (Kadane's Algorithm)
Interview Note: Computes max sum contiguous subarray in O(n) time by maintaining current max and global max.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray_sum(numbers: list[int]) -> int:
    if not numbers:
        return 0
    current = numbers[0]
    maximum = numbers[0]

    for number in numbers[1:]:
        current = max(number, current + number)
        maximum = max(maximum, current)

    return maximum

if __name__ == "__main__":
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Numbers:", numbers)
    print("Max Subarray Sum:", max_subarray_sum(numbers))
