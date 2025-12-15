# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

def max_subarray(nums):
    max_sum = current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print("The maximum subarray sum is:", result)