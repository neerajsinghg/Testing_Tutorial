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