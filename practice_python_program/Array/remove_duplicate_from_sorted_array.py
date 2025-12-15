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