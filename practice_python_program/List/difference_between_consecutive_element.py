# 35. Write a Python program to find the difference between consecutive elements in a list.

my_list = [6,3,98,24,3,5,74,1,5,6,3]

diff_list=[]

for i in range(1,len(my_list)):
   d = my_list[i-1]-my_list[i]
   diff_list.append(d)

print(diff_list)