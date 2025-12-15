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
