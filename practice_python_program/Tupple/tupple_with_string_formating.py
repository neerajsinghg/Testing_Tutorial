# 36. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)
# Create a tuple containing three numbers
t = (100, 200, 300)

# Use the 'format' method to insert the tuple 't' into the string and print the result
print('This is a tuple {0}'.format(t))
# O/p: This is a tuple (100, 200, 300)