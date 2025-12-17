# 31.Write a Python program to convert a tuple to a dictionary.
# Create a tuple containing nested tuples, where each inner tuple consists of two elements.
tuplex = ((2, "w"), (3, "r"))

# Create a dictionary by using a generator expression to swap the elements of each inner tuple.
# The generator iterates through 'tuplex', and for each inner tuple (x, y), it creates a key-value pair (y, x).
result_dict = dict((y, x) for x, y in tuplex)

# Print the resulting dictionary.
print(result_dict)
# O/p: {‘w’: 2, ‘r’: 3}