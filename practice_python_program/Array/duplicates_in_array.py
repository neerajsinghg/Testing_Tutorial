# Find Duplicates in an Array
# Given an array of integers, find all duplicates in the array.

def find_duplicates(arr):
    uniq_set = set()
    duplicate_set = set()
    for num in arr:
        if num in uniq_set:
            duplicate_set.add(num)
        else:
            uniq_set.add(num)
    return list(duplicate_set)

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))

# Another solution with dictionary
from collections import defaultdict
def find_duplicates(arr):
    res = []
    freq_map = defaultdict(int)
    for num in arr:
        freq_map[num] += 1
        # print("this fm :",freq_map)
        if freq_map[num] > 1:
            res.append(num)
    
    return res

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))