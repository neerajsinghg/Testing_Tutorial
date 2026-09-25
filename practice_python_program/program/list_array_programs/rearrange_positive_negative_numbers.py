"""
Interview Question:
Rearrange positive and negative numbers in a list such that all negative numbers appear before positive numbers, preserving relative order.

Interview Explanation:
Sorting algorithms or partitioned array movements while retaining order (stable partitioning) test array manipulation skills.

Key Concepts:
1. Stable Partitioning: O(n) space using list comprehension filtering.
2. In-place modified partition (Two-pointer swap, though order might change).
3. Stable relative ordering vs unstable partitioning.
"""


def rearrange_stable(nums: list) -> list:
    """
    Moves all negative numbers before positive numbers while preserving original order.
    """
    negatives = [x for x in nums if x < 0]
    positives = [x for x in nums if x >= 0]
    return negatives + positives


def rearrange_in_place_two_pointer(nums: list) -> list:
    """
    In-place two-pointer partition (does NOT guarantee relative order retention).
    """
    arr = list(nums)
    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


if __name__ == "__main__":
    sample_nums = [12, 11, -13, -5, 6, -7, 5, -3, -6]

    stable_res = rearrange_stable(sample_nums)
    two_ptr_res = rearrange_in_place_two_pointer(sample_nums)

    print(f"Original List: {sample_nums}")
    print(f"Rearranged (Stable Order):     {stable_res}")
    print(f"Rearranged (In-Place 2-Ptr):  {two_ptr_res}")
