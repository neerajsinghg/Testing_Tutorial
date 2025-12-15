# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1s in the array.

def find_max_consecutive_ones(nums):
    max_count = 0  
    count = 0      
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

nums = [1, 1, 0, 1, 1, 1]
print("Max Consecutive Ones:", find_max_consecutive_ones(nums)) # 3