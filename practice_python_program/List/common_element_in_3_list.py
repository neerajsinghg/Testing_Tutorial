# 30. Write a Python program to find the common elements among three lists.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
list_c = [5, 6, 7, 8, 9,4]

common=list(set(list_a) & set(list_b) & set(list_c))
print(common)