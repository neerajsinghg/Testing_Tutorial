# 10. Write a Python program to remove duplicates from a list.
lst = [6,3,98,24,3,5,74,1,5,6,3]

print(list(set(lst))) #by using set

unique_lst = []
for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)
print(unique_lst)