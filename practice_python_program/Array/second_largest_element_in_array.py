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

# 2nd approches
def second_largest_v3(arr):
    if len(arr) < 2:
        return None

    largest = max(arr)

    # Remove only the FIRST occurrence
    arr_copy = arr.copy()
    arr_copy.remove(largest)

    return max(arr_copy)

print(second_largest_v3([10, 20, 20, 20]))