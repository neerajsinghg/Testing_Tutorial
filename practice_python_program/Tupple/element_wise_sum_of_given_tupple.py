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