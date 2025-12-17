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