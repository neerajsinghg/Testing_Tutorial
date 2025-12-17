# 46. Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# ((‘Red’, ‘White’, ‘Blue’), (‘Green’, ‘Pink’, ‘Purple’), (‘Orange’, ‘Yellow’, ‘Lime’))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
False
# Define a function named 'check_in_tuples' that takes a tuple of tuples 'colors' and a string 'c' as input.
def check_in_tuples(colors, c):
    # Use the 'any' function to check if the string 'c' is present in any of the inner tuples within 'colors'.
    result = any(c in tu for tu in colors)
    
    # Return the result, which is a Boolean indicating whether 'c' is found in any of the inner tuples.
    return result

# Create a tuple of tuples 'colors', where each inner tuple represents a group of colors.
colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)

# Print a message indicating the original list of color tuples.
print("Original list:")
print(colors)

# Define a string 'c1' to check its presence in the color tuples.
c1 = 'White'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))

# Redefine 'c1' to check its presence again.
c1 = 'White'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))

# Redefine 'c1' to check its presence once more with a different value.
c1 = 'Olive'

# Print a message indicating the check for the presence of 'c1' in the tuples of tuples.
print("\nCheck if", c1, "present in said tuple of tuples!")

# Call the 'check_in_tuples' function to check if 'c1' is present in any of the inner tuples and print the result.
print(check_in_tuples(colors, c1))
# O/p: Original list:
# ((‘Red’, ‘White’, ‘Blue’), (‘Green’, ‘Pink’, ‘Purple’), (‘Orange’, ‘Yellow’, ‘Lime’))

# Check if White present in said tuple of tuples!
# True

# Check if White present in said tuple of tuples!
# True

# Check if Olive present in said tuple of tuples!
# False