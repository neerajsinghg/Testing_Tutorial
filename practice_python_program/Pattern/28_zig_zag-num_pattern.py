#Question 28: Zig-Zag Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if (i + j) % 2 == 0:  # Print numbers in zig-zag pattern
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 0 1 0 
0 1 0 1 
1 0 1 0 
0 1 0 1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input to create a zig-zag pattern with numbers.

# The outer loop handles the rows, while the inner loop controls the columns.

# We check if the sum of the row and column indices is even. If so, we print "1"; otherwise, we print "0".

# This creates an alternating pattern of "1"s and "0"s in a zig-zag format across the grid.
