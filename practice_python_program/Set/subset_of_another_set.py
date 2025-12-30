#Question 11: Write a Python program to check if a set is a subset of another set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")     