# 28. Write a Python program to remove the elements at even indices from a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]

output=[mylist[i] for i in range(1,len(mylist),2)]
print(output)