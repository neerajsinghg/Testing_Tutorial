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