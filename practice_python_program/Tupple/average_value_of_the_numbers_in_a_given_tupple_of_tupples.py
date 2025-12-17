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