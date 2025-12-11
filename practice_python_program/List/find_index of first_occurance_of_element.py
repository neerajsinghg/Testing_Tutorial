# 34. Write a Python program to find the index of the first occurrence of an element in a list without using the built-in index function.

my_list = [6,3,98,24,3,5,74,1,5,6,3]
e = 3

for index,value in enumerate(my_list):
  if value==e:
    print(index)
    break