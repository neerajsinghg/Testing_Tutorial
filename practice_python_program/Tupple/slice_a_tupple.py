
# 28.Write a Python program to slice a tuple.
# Create a tuple containing a sequence of numbers
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Use tuple slicing (tuple[start:stop]) to extract a portion of the tuple.
# The start index is inclusive, and the stop index is exclusive.

# Slice from index 3 (inclusive) to 5 (exclusive) and store it in the variable '_slice'
_slice = tuplex[3:5]
print(_slice)

# If the start index isn't defined, it's taken from the beginning of the tuple.
_slice = tuplex[:6]
print(_slice)

# If the end index isn't defined, it's taken until the end of the tuple.
_slice = tuplex[5:]
print(_slice)

# If neither start nor end index is defined, it returns the full tuple.
_slice = tuplex[:]
print(_slice)

# The indexes can be defined with negative values.

# Slice from -8 (inclusive) to -4 (exclusive) and store it in the variable '_slice'
_slice = tuplex[-8:-4]
print(_slice)

# Create another tuple containing the characters of "HELLO WORLD"
tuplex = tuple("HELLO WORLD")
print(tuplex)

# Use step to specify an increment between the elements to cut the tuple.
# tuple[start:stop:step]

# Slice from index 2 to 9 with a step of 2 and store it in the variable '_slice'
_slice = tuplex[2:9:2]
print(_slice)

# Slice with a step of 4, which returns a tuple with a jump every 3 items
_slice = tuplex[::4]
print(_slice)

# When the step is negative, it reverses the order, slicing from index 9 to 2 with a step of -4
_slice = tuplex[9:2:-4]
print(_slice)
# O/p: (5, 4)
# (2, 4, 3, 5, 4, 6)
# (6, 7, 8, 6, 1)
# (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# (3, 5, 4, 6)
# (‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’)
# (‘L’, ‘O’, ‘W’, ‘R’)
# (‘H’, ‘O’, ‘R’)
# (‘L’, ‘ ‘)