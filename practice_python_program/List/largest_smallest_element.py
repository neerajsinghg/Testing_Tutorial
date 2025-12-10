# 2. Write a Python program to find the largest and smallest element in a list.
lst = [8,2,9,3,7]

print("Largest element :", max(lst))
print("Smallest element :", min(lst))

lst1 = sorted(lst, reverse=True)
print(lst1)
print("Largest element :", lst1[0])
print("Smallest element :", lst1[-1])

def largest_no(lst):
    max_no = lst[0]
    for no in lst:
        if no > max_no:
            max_no=no
    return max_no
result = largest_no(lst)
print("largest no by for loop :", result)

def smallest_no(lst):
    min_no = lst[0]
    for no in lst:
        if no < min_no:
            min_no=no
    return min_no

result = smallest_no(lst)
print("smallest no by for loop :", result)