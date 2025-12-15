# 15 Questions on Array to practice before coding interview
# array question for practice

# Find the Most Frequent Element in a List
# Given a list of integers, find the element that appears the most frequently.

from collections import defaultdict
def most_frequent(arr):
    freq_map = defaultdict(int)
    res = None
    curr_max_freq = -1
    for num in arr:
        freq_map[num] += 1
        if freq_map[num] > curr_max_freq:
            res = num
            curr_max_freq = freq_map[num]
    return res

arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
print(most_frequent(arr)) 

# Same with less code and built in function
def most_frequent(arr): 
    return max(set(arr), key=arr.count)
arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
print(most_frequent(arr))

# Find the Missing Number in an Array
# Find the missing number in an array containing ndistinct numbers from 0 to n.

def missing_number(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [3, 0, 1]
print(missing_number(arr))


# Another approach with xor
def missing_number(arr):   
    n = len(arr)
    xor_sum = n
    for i in range(n):
        xor_sum ^= i ^ arr[i]
    return xor_sum

# Example usage
arr = [3, 0, 1]
print(missing_number(arr))

# Find Duplicates in an Array
# Given an array of integers, find all duplicates in the array.

def find_duplicates(arr):
    visited = set()
    duplicates = set()
    for num in arr:
        if num in visited:
            duplicates.add(num)
        else:
            visited.add(num)
    return list(duplicates)

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))

# Another solution with dictionary
from collections import defaultdict
def find_duplicates(arr):
    res = []
    freq_map = defaultdict(int)
    for num in arr:
        freq_map[num] += 1
        if freq_map[num] > 1:
            res.append(num)
    
    return res

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr)) 

# Move Zeroes
# Given an array nums, write a function to move all 0s to the end of it while maintaining the relative order of the non-zero elements.

def move_zeroes(nums):
    zero_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1

nums = [1, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)

# Subarray Sum Equals K
# Given an array of integers numsand an integer k, return the total number of continuous subarrays whose sum equals to k.

def subarray_sum(a, K):
    n = len(a)
    hash = {}
    count, sum = 0, 0
    for i in range(n):
        sum += a[i]
        if sum == K:
            count += 1
        if (sum - K) in hash:
            count += hash[sum - K]
        if sum in hash:
            hash[sum] += 1
        else:
            hash[sum] = 1
    return count

# Example usage:
nums = [1, 1, 1, -1]
k = 2
print(subarray_sum(nums, k))

# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s):
    char_index_map = {}
    start = 0
    max_len = 0

    for idx, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = idx
        max_len = max(max_len, idx - start + 1)

    return max_len

s = "abcabcbb"
print(longest_substring(s))

# Another approach
def longest_substring(s):
    left = 0
    visited = set()
    res = 0
    for idx, char in enumerate(s):
        while char in visited:
            visited.remove(s[left])
            left += 1

        visited.add(char)
        res = max(res, len(visited))
    return res

s = "abcabcbb"
print(longest_substring(s))

# Second Largest
# Write a Python program to find the second largest element in an array. You should solve this problem without sorting the array. If there are duplicate elements, they should be treated as individual values.

def find_second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

# Example usage
arr = [5, 7, 8, 8, 6, 4, 7]
second_largest = find_second_largest(arr)
print("The second largest element is:", second_largest)

# Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. It is the kth largest element in sorted order, not the kth distinct element.

def find_kth_largest(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))

# # Using heap
# def find_kth_largest(nums, k):
#     heap = []
#     for num in nums:
#         heappush(heap, num)
#         if len(heap) > k:
#             heappop(heap)
    
#     return heap[0] if heap else None

# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(find_kth_largest(nums, k)) 

# Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates so each element appears only once. Return the length of the modified array and modify the input array to contain unique elements in the first `k` positions, where `k` is the length of the unique elements.

def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1

# Test the function with an example input
arr = [1, 1, 2, 3, 3, 4]
k = remove_duplicates(arr)
print(f"Number of unique elements: {k}")
print(f"Modified array: {arr[:k]}")


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
target = 9
print(two_sum(nums, target))

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

# Longest Sub-Array with Sum K
# Given an array of integers arr and an integer K, find the length of the longest sub-array whose sum is equal to K. If there is no such sub-array, return 0.

def longest_subarray_with_sum_k(arr, K):
    prefix_sum_map = {}
    curr_sum = 0 
    max_length = 0  
    
    for idx, num in enumerate(arr):
        curr_sum += num
        
        if curr_sum == K:
            max_length = idx + 1
        
        if (curr_sum - K) in prefix_sum_map:
            subarray_length = idx - prefix_sum_map[curr_sum - K]
            max_length = max(max_length, subarray_length)
        
        if curr_sum not in prefix_sum_map:
            prefix_sum_map[curr_sum] = idx
    
    return max_length

arr = [10, 5, 2, 7, 1, 9]
K = 15
result = longest_subarray_with_sum_k(arr, K)
print("The length of the longest sub-array with sum", K, "is:", result)

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

# Union of Two Sorted Arrays with Duplicate Elements
# Given two sorted arrays, arr1 and arr2, write a function to find the union of these two arrays. The union of two arrays is a list that includes all elements from both arrays. Since the arrays are sorted, the union should also be sorted. Duplicates from each array should be preserved in the result.

def union_of_two_sorted_arrays(arr1, arr2):
    
    i, j = 0, 0
    union_result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union_result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union_result.append(arr2[j])
            j += 1
        else:
            union_result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        union_result.append(arr1[i])
        i += 1

    while j < len(arr2):
        union_result.append(arr2[j])
        j += 1

    return union_result

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]
result = union_of_two_sorted_arrays(arr1, arr2)
print("Union of arr1 and arr2:", result)