# 40.Write a Python program to count the elements in a list until an element is a tuple.
# Create a list 'num' that contains a sequence of numbers and a tuple.
num = [10, 20, 30, (10, 20), 40]

# Initialize a counter 'ctr' to keep track of the index of the first tuple in the list.
ctr = 0

# Iterate through each element 'n' in the 'num' list.
for n in num:
    # Check if 'n' is an instance of a tuple.
    if isinstance(n, tuple):
        # If 'n' is a tuple, exit the loop.
        break
    # Increment the counter 'ctr' for non-tuple elements.
    ctr += 1

# Print the value of the 'ctr' variable, which represents the index of the first tuple in the list.
print(ctr) 
# O/p: 3