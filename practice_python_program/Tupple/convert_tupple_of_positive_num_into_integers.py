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