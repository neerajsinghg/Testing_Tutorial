# 41.Write a Python program to convert a given string list to a tuple.
# Original string: python 3.0
# <class ‘str’>
# Convert the said string to a tuple:
# (‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ’n’, ‘3’, ‘.’, ‘0’)
# <class ‘tuple’>
# Define a function named 'string_list_to_tuple' that takes a string 'str1' as input.
def string_list_to_tuple(str1):
    # Create a tuple 'result' by iterating through each character 'x' in 'str1' and excluding whitespaces.
    result = tuple(x for x in str1 if not x.isspace())
    # Return the resulting tuple.
    return result

# Create a string 'str1' with spaces.
str1 = "python 3.0"

# Print the original string.
print("Original string:")
print(str1)

# Print the data type of the 'str1' variable.
print(type(str1))

# Print a message indicating the conversion of the string to a tuple.
print("Convert the said string to a tuple:")

# Call the 'string_list_to_tuple' function to convert the string to a tuple and print the result.
print(string_list_to_tuple(str1))

# Print the data type of the result obtained from the 'string_list_to_tuple' function.
print(type(string_list_to_tuple(str1))) 
# O/p: Original string:
# python 3.0
# <class ‘str’>
# Convert the said string to a tuple:
# (‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ’n’, ‘3’, ‘.’, ‘0’)
# <class ‘tuple’>