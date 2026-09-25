"""
Interview Question:
Find a peak element in a list. An element is a peak if it is strictly greater than its neighbors.

Interview Explanation:
For an unsorted array, finding a peak element can be done in O(n) linearly or O(log n) using binary search logic.

Key Concepts:
1. Boundary condition handling (first and last elements).
2. Binary search approach for logarithmic time O(log n).
"""


def find_peak_element_linear(nums: list) -> int:
    """
    Finds index of first peak element in O(n) time.
    """
    n = len(nums)
    if n == 0:
        return -1
    if n == 1 or nums[0] >= nums[1]:
        return 0
    if nums[n - 1] >= nums[n - 2]:
        return n - 1

    for i in range(1, n - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            return i

    return -1


def find_peak_element_binary_search(nums: list) -> int:
    """
    Finds index of a peak element in O(log n) time using binary search.
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        left_val = nums[mid - 1] if mid > 0 else float('-inf')
        right_val = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')

        if nums[mid] >= left_val and nums[mid] >= right_val:
            return mid
        elif nums[mid] < right_val:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    sample_list = [1, 3, 20, 4, 1, 0]

    peak_idx_lin = find_peak_element_linear(sample_list)
    peak_idx_bs = find_peak_element_binary_search(sample_list)

    print(f"List: {sample_list}")
    print(f"Peak Element (Linear): Index {peak_idx_lin} (Value: {sample_list[peak_idx_lin]})")
    print(f"Peak Element (Binary Search): Index {peak_idx_bs} (Value: {sample_list[peak_idx_bs]})")
