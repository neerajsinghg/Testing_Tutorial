# 21. Write a Python program to find the length of the longest consecutive sequence of elements in a list.

my_list = [100, 4, 200, 1, 3, 2,9,11,12,10,15,13,16,14]
my_list.sort()
print(my_list)
start=0
max_len =0
for i in range(0,len(my_list)-1):
  if my_list[i+1]!=my_list[i]+1:
    end=i
    length = len(my_list[start:end+1])
    max_len = max(length,max_len)
    start=i+1

print(max_len)