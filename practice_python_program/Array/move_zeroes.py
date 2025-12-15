# Move Zeroes
# Given an array nums, write a function to move all 0s to the end of it while maintaining the relative order of the non-zero elements.

def move_zeroes(nums):
    zero_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1

nums = [1, 0,1, 0, 3, 12]
move_zeroes(nums)
print(nums)