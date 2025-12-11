# 14. Write a Python program to find the second smallest element in a list.

lst = [3,6, 4, 5, 6, 7]
lst1 = sorted(lst)
print(lst1[1])

import heapq
second_smallest1 = heapq.nsmallest(2, set(lst))[1]
print(second_smallest1)

first_smallest = float('inf') # float('inf') means positive infinity.
second_smallest = float('inf')
print(first_smallest)
print(second_smallest)
for num in lst:
    if num < first_smallest:
        second_smallest = first_smallest
        first_smallest = num
    elif first_smallest < num < second_smallest:
        second_smallest = num

print("Second smallest:", second_smallest)


        