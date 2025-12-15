# Q4: Unpack the tuple (a, b, c) into three variables and print their values.
my_tuple = ("a", "b", "c")
var1, var2, var3 = my_tuple
print(var1, var2, var3)
# O/p: a b c

# Q19:Write a Python program to unpack a tuple into several variables.
# Create a tuple containing three numbers
tuplex = 4, 8, 3
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Unpack the values from the tuple into the variables n1, n2, and n3
n1, n2, n3 = tuplex
# Calculate and print the sum of n1, n2, and n3
print(n1 + n2 + n3)

# Attempt to unpack the tuple into more variables (n1, n2, n3, and n4)
# This will raise a "ValueError" since there are not enough values in the tuple to unpack into all the variables
n1, n2, n3, n4 = tuplex
# O/p: (4, 8, 3)
# 15