"""
Interview Question:
Find the contiguous subarray within a one-dimensional array of numbers which has the largest sum (Kadane's Algorithm).

Interview Explanation:
Kadane's algorithm is the benchmark optimal solution for finding maximum contiguous subarray sum in O(n) time.

Key Concepts:
1. Dynamic programming concept: local max sum vs global max sum.
2. `current_max = max(num, current_max + num)`
3. `global_max = max(global_max, current_max)`
4. Tracking start and end indices of the maximum subarray.
"""


def max_subarray_sum_kadane(nums: list) -> dict:
    """
    Finds the maximum subarray sum using Kadane's algorithm and returns sum and subarray indices.
    """
    if not nums:
        return {"max_sum": 0, "subarray": []}

    max_so_far = nums[0]
    current_max = nums[0]

    start = end = s = 0

    for i in range(1, len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
            s = i
        else:
            current_max += nums[i]

        if current_max > max_so_far:
            max_so_far = current_max
            start = s
            end = i

    return {
        "max_sum": max_so_far,
        "start_index": start,
        "end_index": end,
        "subarray": nums[start:end + 1]
    }


if __name__ == "__main__":
    sample_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = max_subarray_sum_kadane(sample_arr)

    print(f"Array: {sample_arr}")
    print(f"Maximum Subarray Sum: {result['max_sum']}")
    print(f"Subarray: {result['subarray']} (Indices {result['start_index']} to {result['end_index']})")
