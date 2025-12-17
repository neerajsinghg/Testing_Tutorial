# 42.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple: (4, 3, 2, 2, -1, 18)
# Product — multiplying all the numbers of the said tuple: -864
# Original Tuple: (2, 4, 8, 8, 3, 2, 9)
# Product — multiplying all the numbers of the said tuple: 27648
# Define a function named 'mutiple_tuple' that takes a tuple 'nums' as input.
def mutiple_tuple(nums):
    # Create a temporary list 'temp' by converting the input tuple 'nums' into a list.
    temp = list(nums)
    
    # Initialize a 'product' variable to 1, which will store the product of all numbers in the tuple.
    product = 1 
    
    # Iterate through each element 'x' in the 'temp' list.
    for x in temp:
        # Multiply the current 'x' with the 'product' to accumulate the product of all numbers.
        product *= x
    
    # Return the final product.
    return product

# Create a tuple 'nums' containing a sequence of numbers.
nums = (4, 3, 2, 2, -1, 18)

# Print a message indicating the original tuple.
print ("Original Tuple: ")

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the product, which is the result of multiplying all the numbers in the tuple using the 'mutiple_tuple' function.
print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))

# Create another tuple 'nums' with a different set of numbers.
nums = (2, 4, 8, 8, 3, 2, 9)

# Print a message indicating the original tuple.
print ("\nOriginal Tuple: ")

# Print the 'nums' tuple.
print(nums)

# Print a message indicating the product, which is the result of multiplying all the numbers in the tuple using the 'mutiple_tuple' function.
print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))
# O/p: Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product — multiplying all the numbers of the said tuple: -864

# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product — multiplying all the numbers of the said tuple: 27648
