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