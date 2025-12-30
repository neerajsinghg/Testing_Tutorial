#Question 12: Write a Python program to check if two sets are disjoint.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
my_set = {1, 2, 3, 4, 5}
if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("Sets are not disjoint")

#Question 13: Write a Python program to clear all elements from a set.
my_set.clear()        

#Question 14: Write a Python program to copy a set.
copy_set = my_set.copy()        

#Question 15: Write a Python program to remove and return an arbitrary element from a set.
element = my_set.pop()        

#Question 16: Write a Python program to find the maximum and minimum elements in a set.
maximum = max(my_set)
minimum = min(my_set)        

#Question 17: Write a Python program to find the difference between two sets using the '-' operator.
difference_set = set1 - set2 