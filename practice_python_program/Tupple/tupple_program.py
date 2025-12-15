# Q1: Create a tuple with three elements: 10, “hello”, and 3.14.
my_tuple = (10, "hello", 3.14)

# Q2: Given the tuple (1, 2, 3, 4, 5), access and print the third element.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
# O/p: 3

# Q3: Concatenate the tuples (1, 2, 3) and (4, 5, 6) and store the result in a new tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2

# Q4: Unpack the tuple (a, b, c) into three variables and print their values.
my_tuple = ("a", "b", "c")
var1, var2, var3 = my_tuple
print(var1, var2, var3)
# O/p: a b c

# Q5: Check if the element 7 exists in the tuple (1, 3, 5, 7, 9).
my_tuple = (1, 3, 5, 7, 9)
element_to_check = 7
exists = element_to_check in my_tuple
print(exists)
# O/p: True

# Q6: Create a tuple (0, 1, 2, 3, 4, 5) and print a slice containing elements from index 2 to 4.
my_tuple = (0, 1, 2, 3, 4, 5)
slice_result = my_tuple[2:5]
print(slice_result)
# O/p: (2, 3, 4)

# Q7: Find the length of the tuple (10, 20, 30, 40, 50).
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print(length)
# O/p: 5

# Q8: Create a tuple (1, 2, 3) and repeat it three times.
original_tuple = (1, 2, 3)
repeated_tuple = original_tuple * 3
# Q9: Convert the list [1, 2, 3] to a tuple.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# Q10: Find the minimum and maximum values in the tuple (5, 12, 3, 8, 15).
my_tuple = (5, 12, 3, 8, 15)
min_value = min(my_tuple)
max_value = max(my_tuple)
print("Min:", min_value, "Max:", max_value)
# O/p: Min: 3 Max: 15

# Q11: Count the number of occurrences of the element 2 in the tuple (1, 2, 3, 2, 4, 2).
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print(count_of_2)
# O/p: 3

# Q12: Check if all elements in the tuple (True, True, False) are True.
my_tuple = (True, True, False)
all_true = all(my_tuple)
print(all_true)
# O/p: False

# Q13: Find the index of the first occurrence of the element 3 in the tuple (1, 2, 3, 4, 3, 5).
my_tuple = (1, 2, 3, 4, 3, 5)
index_of_3 = my_tuple.index(3)
print(index_of_3)
# O/p: 2

# Q14: Sort the elements of the tuple (5, 2, 8, 1, 3) and store the result in a new tuple.
my_tuple = (5, 2, 8, 1, 3)
sorted_tuple = tuple(sorted(my_tuple))
# Q15: Create a tuple containing the squares of numbers from 1 to 5.
squares_tuple = tuple(x**2 for x in range(1, 6))

# Q16:Write a Python program to create a tuple.
# Create an empty tuple and assign it to the variable 'x'
x = ()
# Print the contents of the 'x' tuple, which is empty
print(x)

# Create an empty tuple using the tuple() constructor and assign it to the variable 'tuplex'
tuplex = tuple()
# Print the contents of the 'tuplex' tuple, which is also empty
print(tuplex) 
# O/p: (‘tuple’, False, 3.2, 1)

# Q17:Write a Python program to create a tuple with different data types.
# Create a tuple containing elements of different data types
tuplex = ("tuple", False, 3.2, 1)
# Print the contents of the 'tuplex' tuple
print(tuplex)
# O/p: (5, 10, 15, 20, 25)
# (5,)

# Q18:Write a Python program to create a tuple of numbers and print one item.
# Create a tuple containing a sequence of numbers
tuplex = 5, 10, 15, 20, 25
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Create a tuple with a single item (note the comma after the item)
tuplex = 5,
# Print the contents of the 'tuplex' tuple
print(tuplex)
# O/p: (5, 10, 15, 20, 25)
# (5,)

# Q19:Write a Python program to unpack a tuple into several variables.
# Create a tuple containing three numbers
tuplex = 4, 8, 3
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Unpack the values from the tuple into the variables n1, n2, and n3
n1, n2, n3 = tuplex
# Calculate and print the sum of n1, n2, and n3
print(n1 + n2 + n3)

# Attempt to unpack the tuple into more variables (n1, n2, n3, and n4)
# This will raise a "ValueError" since there are not enough values in the tuple to unpack into all the variables
n1, n2, n3, n4 = tuplex
# O/p: (4, 8, 3)
# 15

# Q20:Write a Python program to add an item to a tuple.
# Create a tuple containing a sequence of numbers
tuplex = (4, 6, 2, 8, 3, 1)
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Tuples are immutable, so you can't add new elements directly.
# To add an element, create a new tuple by merging the existing tuple with the desired element using the + operator.
tuplex = tuplex + (9,)
# Print the updated 'tuplex' tuple
print(tuplex)

# Adding items at a specific index in the tuple.
# This line inserts elements (15, 20, 25) between the first five elements and duplicates the original five elements.
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
# Print the modified 'tuplex' tuple
print(tuplex)

# Convert the tuple to a list.
listx = list(tuplex)
# Use different methods to add items to the list.
listx.append(30)
# Convert the modified list back to a tuple to obtain 'tuplex' with the added element.
tuplex = tuple(listx)
# Print the final 'tuplex' tuple with the added element
print(tuplex)
# O/p:(4, 6, 2, 8, 3, 1)
# (4, 6, 2, 8, 3, 1, 9)
# (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3)
# (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3, 30)

# Q21:Write a Python program to convert a tuple to a string.
# Create a tuple containing individual characters
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# Use the 'join' method to concatenate the characters in the tuple without any spaces and create a single string
str = ''.join(tup)
# Print the resulting string
print(str)
# O/p: exercises

# Q22:Write a Python program to get the 4th element from the last element of a tuple.
# Create a tuple containing a sequence of items
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Get the 4th element of the tuple (index 3)
item = tuplex[3]
# Print the value of the 'item'
print(item)

# Get the 4th element from the end of the tuple (index -4)
item1 = tuplex[-4]
# Print the value of the 'item1'
print(item1) 
# o/p: (‘w’, 3, ‘r’, ‘e’, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# e
# u

# Q23:Write a Python program to create the colon of a tuple.
# Import the 'deepcopy' function from the 'copy' module
from copy import deepcopy

# Create a tuple containing various data types
tuplex = ("HELLO", 5, [], True)
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Create a deep copy of the 'tuplex' tuple using the 'deepcopy()' function
tuplex_colon = deepcopy(tuplex)

# Modify the third element of the 'tuplex_colon' tuple, which is a list, by appending the value 50
tuplex_colon[2].append(50)

# Print the 'tuplex_colon' tuple after the modification
print(tuplex_colon)

# Print the original 'tuplex' tuple to demonstrate that it remains unchanged
print(tuplex) 
# O/p: (‘HELLO’, 5, [], True)
# (‘HELLO’, 5, [50], True)
# (‘HELLO’, 5, [], True)











































































# Q24:Write a Python program to find repeated items in a tuple.
# Create a tuple containing a sequence of numbers
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Count the number of times the value 4 appears in the 'tuplex' tuple
count = tuplex.count(4)
# Print the count of how many times 4 appears
print(count) 
# O/p: (2, 4, 5, 6, 2, 3, 4, 4, 7)
# 3

# Q25:Write a Python program to check whether an element exists within a tuple.
# Create a tuple containing a sequence of items
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")

# Check if the character "r" is present in the 'tuplex' tuple and print the result
print("r" in tuplex)

# Check if the number 5 is present in the 'tuplex' tuple and print the result
print(5 in tuplex)
# O/p: True
False

# Q26:Write a Python program to convert a list to a tuple.
# Create a list containing a sequence of numbers
listx = [5, 10, 7, 4, 15, 3]
# Print the contents of the 'listx' list
print(listx)

# Use the 'tuple()' function, a built-in Python function, to convert the 'listx' list to a tuple
tuplex = tuple(listx)
# Print the contents of the 'tuplex' tuple
print(tuplex)
# O/p: [5, 10, 7, 4, 15, 3]
# (5, 10, 7, 4, 15, 3)

# Q27.Write a Python program to remove an item from a tuple.
# Create a tuple containing a sequence of items
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Tuples are immutable, so you cannot remove elements directly.
# To "remove" an item, create a new tuple by merging the desired elements using the + operator.
tuplex = tuplex[:2] + tuplex[3:]
# Print the updated 'tuplex' tuple
print(tuplex)

# Convert the 'tuplex' tuple to a list
listx = list(tuplex)
# Use the 'remove' method to eliminate the item "c" from the list
listx.remove("c")
# Convert the modified list back to a tuple to obtain 'tuplex' with the item removed
tuplex = tuple(listx)
# Print the final 'tuplex' tuple
print(tuplex) 
# O/p: (‘w’, 3, ‘r’, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# (‘w’, 3, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# (‘w’, 3, ‘s’, ‘o’, ‘u’, ‘r’, ‘e’)

# 28.Write a Python program to slice a tuple.
# Create a tuple containing a sequence of numbers
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Use tuple slicing (tuple[start:stop]) to extract a portion of the tuple.
# The start index is inclusive, and the stop index is exclusive.

# Slice from index 3 (inclusive) to 5 (exclusive) and store it in the variable '_slice'
_slice = tuplex[3:5]
print(_slice)

# If the start index isn't defined, it's taken from the beginning of the tuple.
_slice = tuplex[:6]
print(_slice)

# If the end index isn't defined, it's taken until the end of the tuple.
_slice = tuplex[5:]
print(_slice)

# If neither start nor end index is defined, it returns the full tuple.
_slice = tuplex[:]
print(_slice)

# The indexes can be defined with negative values.

# Slice from -8 (inclusive) to -4 (exclusive) and store it in the variable '_slice'
_slice = tuplex[-8:-4]
print(_slice)

# Create another tuple containing the characters of "HELLO WORLD"
tuplex = tuple("HELLO WORLD")
print(tuplex)

# Use step to specify an increment between the elements to cut the tuple.
# tuple[start:stop:step]

# Slice from index 2 to 9 with a step of 2 and store it in the variable '_slice'
_slice = tuplex[2:9:2]
print(_slice)

# Slice with a step of 4, which returns a tuple with a jump every 3 items
_slice = tuplex[::4]
print(_slice)

# When the step is negative, it reverses the order, slicing from index 9 to 2 with a step of -4
_slice = tuplex[9:2:-4]
print(_slice)
# O/p: (5, 4)
# (2, 4, 3, 5, 4, 6)
# (6, 7, 8, 6, 1)
# (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# (3, 5, 4, 6)
# (‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’)
# (‘L’, ‘O’, ‘W’, ‘R’)
# (‘H’, ‘O’, ‘R’)
# (‘L’, ‘ ‘)

# 29.Write a Python program to find the index of an item in a tuple.
# Create a tuple by converting the string "index tuple" into a tuple
tuplex = tuple("index tuple")
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Get the index of the first occurrence of the character "p" in the 'tuplex' tuple
index = tuplex.index("p")
# Print the index value
print(index)

# Define the index from which you want to start searching for the character "p" (index 5)
index = tuplex.index("p", 5)
# Print the index value
print(index)

# Define a segment of the 'tuplex' tuple (from index 3 to 6) within which you want to search for the character "e"
index = tuplex.index("e", 3, 6)
# Print the index value
print(index)

# Attempt to find the index of the character "y," which does not exist in the 'tuplex' tuple
# This will raise a "ValueError" exception because the item is not in the tuple
index = tuplex.index("y")
# O/p: (‘i’, ’n’, ‘d’, ‘e’, ‘x’, ‘ ‘, ‘t’, ‘u’, ‘p’, ‘l’, ‘e’)
# 8
# 8
# 3

# 30.Write a Python program to find the length of a tuple.
# Create a tuple by converting the string "w3resource" into a tuple
tuplex = tuple("w3resource")
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Use the 'len()' function to determine the length of the 'tuplex' tuple
print(len(tuplex)) 
# O/p: (‘w’, ‘3’, ‘r’, ‘e’, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# 10

# 31.Write a Python program to convert a tuple to a dictionary.
# Create a tuple containing nested tuples, where each inner tuple consists of two elements.
tuplex = ((2, "w"), (3, "r"))

# Create a dictionary by using a generator expression to swap the elements of each inner tuple.
# The generator iterates through 'tuplex', and for each inner tuple (x, y), it creates a key-value pair (y, x).
result_dict = dict((y, x) for x, y in tuplex)

# Print the resulting dictionary.
print(result_dict)
# O/p: {‘w’: 2, ‘r’: 3}

# 32.Write a Python program to unzip a list of tuples into individual lists.
# Create a list of tuples, where each tuple contains two elements.
l = [(1, 2), (3, 4), (8, 9)]

# Use the 'zip' function with the '*' operator to unpack and zip the tuples.
# This creates new tuples where the first elements from the original tuples are combined into one tuple,
# and the second elements from the original tuples are combined into another tuple.
result = list(zip(*l))

# Print the result, which is a list of two tuples formed by zipping the original tuples.
print(result)
# O/p: [(1, 3, 8), (2, 4, 9)]

# 33. Write a Python program to reverse a tuple.
# Create a tuple containing a single string
x = ("w3resource")

# Reverse the characters in the string by using the 'reversed' function,
# and then convert the reversed object back into a tuple and print it.
y = reversed(x)
print(tuple(y))

# Create another tuple containing a sequence of numbers
x = (5, 10, 15, 20)

# Reverse the order of the elements in the tuple using the 'reversed' function,
# and then convert the reversed object back into a tuple and print it.
y = reversed(x)
print(tuple(y))
# O/p: (‘e’, ‘c’, ‘r’, ‘u’, ‘o’, ‘s’, ‘e’, ‘r’, ‘3’, ‘w’)
# (20, 15, 10, 5)

# 34.Write a Python program to convert a list of tuples into a dictionary.
# Create a list of tuples where each tuple contains two elements, a character and a number.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

# Create an empty dictionary to store the results.
d = {}

# Iterate through each tuple (a, b) in the list 'l'.
for a, b in l:
    # Use 'setdefault' to create an empty list in the dictionary 'd' for the key 'a' if it doesn't exist.
    # Then, append the value 'b' to the list associated with key 'a'.
    d.setdefault(a, []).append(b)

# Print the resulting dictionary, where keys represent characters, and values are lists of corresponding numbers.
print(d) 
# O/p: {‘x’: [1, 2, 3], ‘y’: [1, 2], ‘z’: [1]}

# 35.Write a Python program to convert a list of tuples into a dictionary.
# Create a tuple containing three numbers
t = (100, 200, 300)

# Use the 'format' method to insert the tuple 't' into the string and print the result
print('This is a tuple {0}'.format(t))
# O/p: This is a tuple (100, 200, 300)

# 36. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)
# Create a tuple containing three numbers
t = (100, 200, 300)

# Use the 'format' method to insert the tuple 't' into the string and print the result
print('This is a tuple {0}'.format(t))
# O/p: This is a tuple (100, 200, 300)

# 37.Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# Create a list of tuples, where each tuple contains three numbers.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Use a list comprehension to iterate through each tuple 't' in the list 'l'.
# For each tuple, create a new tuple by removing the last element and adding the number 100.
# The result is a list of modified tuples.
print([t[:-1] + (100,) for t in l]) 
# O/p: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# 38.Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), (‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), (‘d’)]
# Expected output: [(‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), ‘d’]
# Create a list 'L' containing various elements, including empty tuples and tuples with strings.

# Use a list comprehension to filter out the empty tuples by checking if each tuple 't' in 'L' is not empty.
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# Print the modified list 'L' after removing the empty tuples.
L = [t for t in L if t]
print(L)
# O/p: [(‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), ‘d’]

# 39.Write a Python program to sort a tuple by its float element.
# Sample data: [(‘item1’, ‘12.20’), (‘item2’, ‘15.10’), (‘item3’, ‘24.5’)]
# Expected Output: [(‘item3’, ‘24.5’), (‘item2’, ‘15.10’), (‘item1’, ‘12.20’)]
# Create a list of tuples 'price', where each tuple represents an item and its price as a string.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Sort the 'price' list based on the price values (the second element in each tuple).
# The 'key' argument specifies a lambda function to convert the price strings to float values.
# Sorting is done in reverse (descending) order using the 'reverse' argument.
sorted_price = sorted(price, key=lambda x: float(x[1]), reverse=True)

# Print the 'sorted_price' list, which contains the items sorted by price in descending order.
print(sorted_price)
# O/p:[(‘item3’, ‘24.5’), (‘item2’, ‘15.10’), (‘item1’, ‘12.20’)]

# 40.Write a Python program to count the elements in a list until an element is a tuple.
# Create a list 'num' that contains a sequence of numbers and a tuple.
num = [10, 20, 30, (10, 20), 40]

# Initialize a counter 'ctr' to keep track of the index of the first tuple in the list.
ctr = 0

# Iterate through each element 'n' in the 'num' list.
for n in num:
    # Check if 'n' is an instance of a tuple.
    if isinstance(n, tuple):
        # If 'n' is a tuple, exit the loop.
        break
    # Increment the counter 'ctr' for non-tuple elements.
    ctr += 1

# Print the value of the 'ctr' variable, which represents the index of the first tuple in the list.
print(ctr) 
# O/p: 3

# 41.Write a Python program to convert a given string list to a tuple.
# Original string: python 3.0
# <class ‘str’>
# Convert the said string to a tuple:
# (‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ’n’, ‘3’, ‘.’, ‘0’)
# <class ‘tuple’>
# Define a function named 'string_list_to_tuple' that takes a string 'str1' as input.
def string_list_to_tuple(str1):
    # Create a tuple 'result' by iterating through each character 'x' in 'str1' and excluding whitespaces.
    result = tuple(x for x in str1 if not x.isspace())
    # Return the resulting tuple.
    return result

# Create a string 'str1' with spaces.
str1 = "python 3.0"

# Print the original string.
print("Original string:")
print(str1)

# Print the data type of the 'str1' variable.
print(type(str1))

# Print a message indicating the conversion of the string to a tuple.
print("Convert the said string to a tuple:")

# Call the 'string_list_to_tuple' function to convert the string to a tuple and print the result.
print(string_list_to_tuple(str1))

# Print the data type of the result obtained from the 'string_list_to_tuple' function.
print(type(string_list_to_tuple(str1))) 
# O/p: Original string:
# python 3.0
# <class ‘str’>
# Convert the said string to a tuple:
# (‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ’n’, ‘3’, ‘.’, ‘0’)
# <class ‘tuple’>

# 42.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple: (4, 3, 2, 2, -1, 18)
# Product — multiplying all the numbers of the said tuple: -864
# Original Tuple: (2, 4, 8, 8, 3, 2, 9)
# Product — multiplying all the numbers of the said tuple: 27648
# Define a function named 'mutiple_tuple' that takes a tuple 'nums' as input.
def mutiple_tuple(nums):
    # Create a temporary list 'temp' by converting the input tuple 'nums' into a list.
    temp = list(nums)
    
    # Initialize a 'product' variable to 1, which will store the product of all numbers in the tuple.
    product = 1 
    
    # Iterate through each element 'x' in the 'temp' list.
    for x in temp:
        # Multiply the current 'x' with the 'product' to accumulate the product of all numbers.
        product *= x
    
    # Return the final product.
    return product

# Create a tuple 'nums' containing a sequence of numbers.
nums = (4, 3, 2, 2, -1, 18)

# Print a message indicating the original tuple.
print ("Original Tuple: ")

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the product, which is the result of multiplying all the numbers in the tuple using the 'mutiple_tuple' function.
print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))

# Create another tuple 'nums' with a different set of numbers.
nums = (2, 4, 8, 8, 3, 2, 9)

# Print a message indicating the original tuple.
print ("\nOriginal Tuple: ")

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the product, which is the result of multiplying all the numbers in the tuple using the 'mutiple_tuple' function.
print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))
# O/p: Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product — multiplying all the numbers of the said tuple: -864

# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product — multiplying all the numbers of the said tuple: 27648

# 43.Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]
# Define a function named 'average_tuple' that takes a tuple of tuples 'nums' as input.
def average_tuple(nums):
    # Calculate the average values of the numbers within the 'nums' tuple of tuples.
    # Use list comprehension to calculate the sum of elements for each position across all inner tuples,
    # and then divide by the number of inner tuples to get the average for each position.
    result = [sum(x) / len(x) for x in zip(*nums)]
    
    # Return the list of average values.
    return result

# Create a tuple of tuples 'nums' containing four inner tuples with numbers.
nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# Print a message indicating the original tuple.
print ("Original Tuple: ")

# Print the 'nums' tuple of tuples.
print(nums)

# Print a message indicating the average values, which are calculated using the 'average_tuple' function.
print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums))

# Create another tuple of tuples 'nums' with a different set of numbers.
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

# Print a message indicating the original tuple.
print ("\nOriginal Tuple: ")

# Print the 'nums' tuple of tuples.
print(nums)

# Print a message indicating the average values, which are calculated using the 'average_tuple' function.
print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums))
# O/p: Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]

# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]

# 44.Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# ((‘333’, ‘33’), (‘1416’, ‘55’))
# New tuple values:
((333, 33), (1416, 55))
# Define a function named 'tuple_int_str' that takes a tuple of tuples 'tuple_str' as input.
def tuple_int_str(tuple_str):
    # Create a new tuple 'result' by converting the string elements in each inner tuple to integers.
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    
    # Return the resulting tuple.
    return result

# Create a tuple of tuples 'tuple_str' containing pairs of strings.
tuple_str = (('333', '33'), ('1416', '55'))

# Print a message indicating the original tuple values.
print("Original tuple values:")

# Print the 'tuple_str' tuple.
print(tuple_str)

# Print a message indicating the new tuple values, which are obtained by converting the strings to integers using the 'tuple_int_str' function.
print("\nNew tuple values:")

# Call the 'tuple_int_str' function to convert the strings to integers and print the result.
print(tuple_int_str(tuple_str))
# O/p: Original tuple values:
# ((‘333’, ‘33’), (‘1416’, ‘55’))

# New tuple values:
# ((333, 33), (1416, 55))

# 45. Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570
# Define a function named 'tuple_to_int' that takes a tuple 'nums' as input.
def tuple_to_int(nums):
    # Convert the tuple elements to a single integer by joining them as strings,
    # mapping each element to a string, and then converting the result to an integer.
    result = int(''.join(map(str, nums)))
    
    # Return the resulting integer.
    return result

# Create a tuple 'nums' containing positive integers.
nums = (1, 2, 3)

# Print a message indicating the original tuple of positive integers.
print("Original tuple: ") 

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the conversion of the tuple to an integer using the 'tuple_to_int' function.
print("Convert the said tuple of positive integers into an integer:")

# Call the 'tuple_to_int' function to convert the tuple to an integer and print the result.
print(tuple_to_int(nums))

# Create another tuple 'nums' with a different set of positive integers.
nums = (10, 20, 40, 5, 70)

# Print a message indicating the original tuple of positive integers.
print("\nOriginal tuple: ") 

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the conversion of the tuple to an integer using the 'tuple_to_int' function.
print("Convert the said tuple of positive integers into an integer:")

# Call the 'tuple_to_int' function to convert the tuple to an integer and print the result.
print(tuple_to_int(nums))
# O/p:Original tuple:
# (1, 2, 3)

# 46. Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# ((‘Red’, ‘White’, ‘Blue’), (‘Green’, ‘Pink’, ‘Purple’), (‘Orange’, ‘Yellow’, ‘Lime’))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
False
# Define a function named 'check_in_tuples' that takes a tuple of tuples 'colors' and a string 'c' as input.
def check_in_tuples(colors, c):
    # Use the 'any' function to check if the string 'c' is present in any of the inner tuples within 'colors'.
    result = any(c in tu for tu in colors)
    
    # Return the result, which is a Boolean indicating whether 'c' is found in any of the inner tuples.
    return result

# Create a tuple of tuples 'colors', where each inner tuple represents a group of colors.
colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)

# Print a message indicating the original list of color tuples.
print("Original list:")
print(colors)

# Define a string 'c1' to check its presence in the color tuples.
c1 = 'White'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))

# Redefine 'c1' to check its presence again.
c1 = 'White'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))

# Redefine 'c1' to check its presence once more with a different value.
c1 = 'Olive'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))
# O/p: Original list:
# ((‘Red’, ‘White’, ‘Blue’), (‘Green’, ‘Pink’, ‘Purple’), (‘Orange’, ‘Yellow’, ‘Lime’))

# Check if White present in said tuple of tuples!
# True

# Check if White present in said tuple of tuples!
# True

# Check if Olive present in said tuple of tuples!
# False

# 47. Write a Python program to compute the element-wise sum of given tuples.
# Original lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
(6, 9, 8, 6)
# Define three tuples 'x', 'y', and 'z' with integer elements.
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

# Print a message indicating the original lists of tuples.
print("Original lists:")
print(x)
print(y)
print(z)

# Print a message indicating the element-wise sum of the said tuples.

# Use the 'zip' function to pair corresponding elements from 'x', 'y', and 'z' tuples, and then use 'map' and 'sum' to calculate the element-wise sum.
result = tuple(map(sum, zip(x, y, z)))

# Print the 'result' tuple containing the element-wise sum.
print("\nElement-wise sum of the said tuples:")
print(result)
# O/p: Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)

# Element-wise sum of the said tuples:
(6, 9, 8, 6)

# 48.Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
# Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]
# Original list of tuples:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [9, -1, 7, 8]
# Define a function named 'test' that takes a list of tuples 'lst' as input.
def test(lst):
    # Use 'map' to calculate the sum of elements within each tuple in the list.
    result = map(sum, lst)
    
    # Convert the result to a list.
    return list(result)

# Create a list of tuples 'nums' containing tuples of integers.
nums = [(1, 2), (2, 3), (3, 4)]

# Print a message indicating the original list of tuples.
print("Original list of tuples:")
print(nums)

# Print a message indicating the sum of all elements in each tuple stored inside the list of tuples.

# Call the 'test' function to calculate the sums and convert the result to a list, then print it.
print("\nSum of all the elements of each tuple stored inside the said list of tuples:")
print(test(nums))

# Create another list of tuples 'nums' with a different set of tuples, including varying numbers of elements.
nums = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

# Print a message indicating the original list of tuples.
print("\nOriginal list of tuples:")
print(nums)

# Print a message indicating the sum of all elements in each tuple stored inside the list of tuples.

# Call the 'test' function to calculate the sums and convert the result to a list, then print it.
print("\nSum of all the elements of each tuple stored inside the said list of tuples:")
print(test(nums))
# O/p: Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]

# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]

# Original list of tuples:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

# Sum of all the elements of each tuple stored inside the said list of tuples:
# [9, -1, 7, 8]

# 49.Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
# Define a function named 'test' that takes a list of tuples 'lst_tuples' as input.
def test(lst_tuples):
    # Use a list comprehension to convert each tuple in 'lst_tuples' to a list.
    result = [list(el) for el in lst_tuples]
    
    # Return the resulting list of lists.
    return result

# Create a list of tuples 'lst_tuples' containing tuples of integers.
lst_tuples = [(1, 2), (2, 3), (3, 4)]

# Print a message indicating the original list of tuples.
print("Original list of tuples:")
print(lst_tuples)

# Print a message indicating the conversion of the list of tuples to a list of lists.

# Call the 'test' function to perform the conversion and print the result.
print("Convert the said list of tuples to a list of lists:")
print(test(lst_tuples))

# Create another list of tuples 'lst_tuples' with a different set of tuples, including varying numbers of elements.
lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

# Print a message indicating the original list of tuples.
print("\nOriginal list of tuples:")
print(lst_tuples)

# Print a message indicating the conversion of the list of tuples to a list of lists.

# Call the 'test' function to perform the conversion and print the result.
print("Convert the said list of tuples to a list of lists:")
print(test(lst_tuples))
# O/p: Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists:
# [[1, 2], [2, 3], [3, 4]]

# Original list of tuples:
# [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists:
# [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]