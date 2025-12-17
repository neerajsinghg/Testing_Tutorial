#Question 29: Cross Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == j or i + j == rows + 1:  # Print stars in cross pattern
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space
    print()


'''''''''Output:
Enter the row size for the pattern: 5
*       * 
  *   *   
    *     
  *   *   
*       * 

=== Code Execution Successful ==='''

# Code Explanation: 
# We start by taking the row input for the pattern.

# The outer loop controls the rows, and the inner loop handles the columns.

# We check two conditions: if the row number equals the column number, or if their sum equals the total rows plus one. If either is true, we print a star(“*”).

# This creates a cross pattern with stars in the grid, with spaces in other positions.
