# 4. Write a Python program to find the index of an element in a list.
lst = ['A','P','B','Q','C','D']

print("index of b :", lst.index("B"))

for i in range(len(lst)):
    if lst[i]=="B":
        print("index of B :", i)