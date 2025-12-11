# 29. Write a Python program to find the sum of elements at odd indices in a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
total = mylist[1::2]
print(total)
print(sum(total))