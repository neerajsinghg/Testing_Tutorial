"""
Interview Question:
Find the length of the longest increasing contiguous subarray in a list of numbers.

Interview Explanation:
Tracking consecutive sequence lengths in test execution results or timestamped data logs is a standard data processing task.

Key Concepts:
1. Continuous iteration tracking `current_len` and `max_len`.
2. Resetting `current_len` to 1 whenever an element is not greater than its predecessor.
3. Time Complexity: O(n), Space Complexity: O(1).
"""


def longest_increasing_subarray(nums: list) -> dict:
    """
    Returns the maximum length and the contiguous increasing subarray.
    """
    if not nums:
        return {"length": 0, "subarray": []}

    max_len = 1
    current_len = 1

    max_start = 0
    current_start = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
        else:
            current_len = 1
            current_start = i

    return {
        "length": max_len,
        "subarray": nums[max_start:max_start + max_len]
    }


if __name__ == "__main__":
    sample_list = [10, 20, 30, 5, 8, 9, 12, 15, 2]

    res = longest_increasing_subarray(sample_list)
    print(f"List: {sample_list}")
    print(f"Longest Increasing Subarray Length: {res['length']}")
    print(f"Subarray: {res['subarray']}")
