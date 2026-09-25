"""
17. Find Missing Number in a Sequence (1 to n)
Interview Note: Uses Gauss formula n*(n+1)//2 to find expected sum vs actual sum in O(n) time and O(1) space.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_missing_number(numbers: list[int]) -> int:
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 6]
    print("Input:", numbers)
    print("Missing Number:", find_missing_number(numbers))
