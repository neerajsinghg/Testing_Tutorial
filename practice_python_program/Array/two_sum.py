# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return None

nums = [2, 7, 11, 15]
target = 13
print(two_sum(nums, target))