# 12. Write a Python program to find the common elements between two lists.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common_ele = []
for el1 in list_a:
    if el1 in list_b:
            common_ele.append(el1)
print(common_ele)


common_ele1 = []
for el1 in list_a:
    for el2 in list_b:
        if el1==el2:
            common_ele1.append(el2)
print(common_ele1)

common = list(set(list_a) & set(list_b))
print(common)