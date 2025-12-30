#Question 20: Write a Python program to find the common elements between multiple sets.
set3 = {2, 8, 7, 9}
set1 = {1, 2, 3}
set2 = {3, 4, 5}
common_elements = set.intersection(set1, set2, set3) 

#Question 21: Write a Python program to remove the intersection of two sets from one set.
set1.difference_update(set2)        

#Question 22: Write a Python program to create a frozen set.
frozen_set = frozenset([1, 2, 3])