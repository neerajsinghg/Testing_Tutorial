# 31. Write a Python program to find the k smallest elements in a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
k=3
mylist.sort()
print(f"{k}th smallest element: ",mylist[k-1])