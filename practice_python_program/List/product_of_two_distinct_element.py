# 33. Write a Python program to find the largest product of two distinct elements in a list.

my_list = [1, 2, 3, 4, 5]

my_list.sort()

p_max = my_list[-1] * my_list[-2]
print(p_max)