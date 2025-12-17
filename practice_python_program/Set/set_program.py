set 
# Question 1: Write a Python program to create an empty set.

my_set = set()        

# Question 2: Write a Python program to create a set with elements "apple", "banana", and "cherry".

fruits = {"apple", "banana", "cherry"}  

# Question 3: Write a Python program to find the length of a set.

my_set = {1, 2, 3, 4, 5}
length = len(my_set)
print(length)        

#Question 4: Write a Python program to add an element to a set.

my_set.add(6)    

#Question 5: Write a Python program to remove an element from a set.

my_set.remove(3)   

#Question 6: Write a Python program to check if an element is present in a set.

if 4 in my_set:
    print("Element found")
else:
    print("Element not found")  

#Question 7: Write a Python program to perform set union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)       

#Question 8: Write a Python program to perform set intersection.
intersection_set = set1.intersection(set2)        

#Question 9: Write a Python program to perform set difference.
difference_set = set1.difference(set2)        

#Question 10: Write a Python program to perform symmetric difference.
symmetric_difference_set = set1.symmetric_difference(set2)  

#Question 11: Write a Python program to check if a set is a subset of another set.
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")     

#Question 12: Write a Python program to check if two sets are disjoint.
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

#Question 18: Write a Python program to update a set with elements from another iterable.
new_elements = [6, 7, 8]
my_set.update(new_elements)        

#Question 19: Write a Python program to remove a specific element from a set using the discard method.
my_set.discard(6)        

#Question 20: Write a Python program to find the common elements between multiple sets.
set3 = {2, 8, 7, 9}
common_elements = set.intersection(set1, set2, set3)   

#Question 21: Write a Python program to remove the intersection of two sets from one set.
set1.difference_update(set2)        

#Question 22: Write a Python program to create a frozen set.
frozen_set = frozenset([1, 2, 3])        

#Question 23: Write a Python program to convert a list into a set.
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)        

#Question 24: Write a Python program to find the union of multiple sets.
union_set = set.union(set1, set2, set3)        

#Question 25: Write a Python program to check if two sets are equal.
if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")      