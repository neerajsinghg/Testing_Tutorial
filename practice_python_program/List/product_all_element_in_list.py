# 16. Write a Python program to find the product of all elements in a list.

lst = [3,6, 4, 5, 6, 7]
product = 1
for num in lst:
    product *= num
print(product)