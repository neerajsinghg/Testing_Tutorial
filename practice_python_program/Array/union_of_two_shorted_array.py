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

arr3 = sorted(set(arr1).union(set(arr2)))
print(arr3)