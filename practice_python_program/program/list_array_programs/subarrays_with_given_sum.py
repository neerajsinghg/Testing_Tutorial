"""
Interview Question:
Find a contiguous subarray whose sum equals a target value S in a list of non-negative integers.

Interview Explanation:
Sliding window technique for contiguous subarray problems is a favorite interview topic for SDETs analyzing sequence datasets.

Key Concepts:
1. Two-pointer / Sliding Window technique: `start` and `end`.
2. Expand window by moving `end` right; shrink window by moving `start` right when current sum exceeds target.
3. Time Complexity: O(n) linear scan, Space Complexity: O(1).
"""


def find_subarray_with_target_sum(nums: list, target_sum: int) -> tuple:
    """
    Returns (start_index, end_index, subarray) for first contiguous subarray matching target_sum.
    """
    start = 0
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum > target_sum and start <= end:
            current_sum -= nums[start]
            start += 1

        if current_sum == target_sum:
            return (start, end, nums[start:end + 1])

    return (-1, -1, [])


if __name__ == "__main__":
    sample_list = [1, 4, 20, 3, 10, 5]
    target = 33

    start_idx, end_idx, sub_arr = find_subarray_with_target_sum(sample_list, target)

    print(f"List: {sample_list} | Target Sum: {target}")
    if sub_arr:
        print(f"Subarray found from index {start_idx} to {end_idx}: {sub_arr}")
    else:
        print("No subarray found with matching sum.")
