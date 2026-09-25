"""
Interview Question:
Given an array containing n distinct numbers taken from the range 1 to n+1, find the one missing number.

Interview Explanation:
In automation testing (e.g., verifying sequential transaction IDs, sequence numbering, or order IDs in database records), identifying missing sequence gaps is a standard validation task.

Key Concepts:
1. Mathematical formula method: Sum of first N numbers = N * (N + 1) // 2.
2. XOR method: Avoiding integer overflow issues.
3. Time Complexity: O(n), Space Complexity: O(1).
"""


def find_missing_number_sum(nums: list) -> int:
    """
    Finds missing number in 1 to N+1 sequence using mathematical sum formula.
    """
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def find_missing_number_xor(nums: list) -> int:
    """
    Finds missing number using bitwise XOR operator (handles large numbers safely).
    """
    n = len(nums) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    for num in nums:
        xor_all ^= num

    return xor_all


if __name__ == "__main__":
    sample_sequence = [1, 2, 4, 5, 6, 7, 8]  # 3 is missing

    missing_sum = find_missing_number_sum(sample_sequence)
    missing_xor = find_missing_number_xor(sample_sequence)

    print(f"Sequence: {sample_sequence}")
    print(f"Missing Number (Sum Method): {missing_sum}")
    print(f"Missing Number (XOR Method): {missing_xor}")
