# Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. It is the kth largest element in sorted order, not the kth distinct element.

def find_kth_largest(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))