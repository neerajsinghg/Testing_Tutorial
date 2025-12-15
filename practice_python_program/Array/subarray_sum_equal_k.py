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