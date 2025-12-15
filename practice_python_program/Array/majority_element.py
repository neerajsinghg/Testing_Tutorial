# Majority Element
# Given an integer array nums, find all elements that appear more than n/3 times.

def majorityElement(nums):
    dict = {}
    result  = []
    for candidate in nums:
        if candidate in dict:
            dict[candidate] += 1
        else:
            dict[candidate] = 1
    for key in dict:
        if dict[key] > len(nums)//3:
            result .append(key)
    return result 

nums = [1, 1, 1, 3, 3, 2, 2, 2]
print("\nInput:", nums)
print("Output:", majorityElement(nums))  # Output: [1, 2]

def majorityElement(nums):
    if not nums:
        return []

    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    threshold = len(nums) // 3
    if count1 > threshold:
        result.append(candidate1)
    if count2 > threshold and candidate2 != candidate1:
        result.append(candidate2)

    return result

nums = [1, 1, 1, 3, 3, 2, 2, 2]
print("\nInput:", nums)
print("Output:", majorityElement(nums))