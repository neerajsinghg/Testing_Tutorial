# Q27.Write a Python program to remove an item from a tuple.
# Create a tuple containing a sequence of items
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Tuples are immutable, so you cannot remove elements directly.
# To "remove" an item, create a new tuple by merging the desired elements using the + operator.
tuplex = tuplex[:2] + tuplex[3:]
# Print the updated 'tuplex' tuple
print(tuplex)

# Convert the 'tuplex' tuple to a list
listx = list(tuplex)
# Use the 'remove' method to eliminate the item "c" from the list
listx.remove("c")
# Convert the modified list back to a tuple to obtain 'tuplex' with the item removed
tuplex = tuple(listx)
# Print the final 'tuplex' tuple
print(tuplex) 
# O/p: (‘w’, 3, ‘r’, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# (‘w’, 3, ‘s’, ‘o’, ‘u’, ‘r’, ‘c’, ‘e’)
# (‘w’, 3, ‘s’, ‘o’, ‘u’, ‘r’, ‘e’)