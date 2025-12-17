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