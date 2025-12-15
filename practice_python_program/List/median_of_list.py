# 27. Write a Python program to find the median of a list.

my_list = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,17,18,19]
my_list.sort()

length = len(my_list)
if len(my_list)%2!=0:
  med = my_list[(length//2)]
else:
    med = (my_list[length//2]+my_list[(length//2)-1])/2

print(med)