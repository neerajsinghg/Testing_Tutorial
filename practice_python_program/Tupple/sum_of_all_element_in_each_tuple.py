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