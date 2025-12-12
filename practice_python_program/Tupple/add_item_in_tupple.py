# Q20:Write a Python program to add an item to a tuple.
# Create a tuple containing a sequence of numbers
tuplex = (4, 6, 2, 8, 3, 1)
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Tuples are immutable, so you can't add new elements directly.
# To add an element, create a new tuple by merging the existing tuple with the desired element using the + operator.
tuplex = tuplex + (9,)
# Print the updated 'tuplex' tuple
print(tuplex)

# Adding items at a specific index in the tuple.
# This line inserts elements (15, 20, 25) between the first five elements and duplicates the original five elements.
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
# Print the modified 'tuplex' tuple
print(tuplex)

# Convert the tuple to a list.
listx = list(tuplex)
# Use different methods to add items to the list.
listx.append(30)
# Convert the modified list back to a tuple to obtain 'tuplex' with the added element.
tuplex = tuple(listx)
# Print the final 'tuplex' tuple with the added element
print(tuplex)
# O/p:(4, 6, 2, 8, 3, 1)
# (4, 6, 2, 8, 3, 1, 9)
# (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3)
# (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3, 30)