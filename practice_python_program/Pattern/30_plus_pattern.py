#Question 30: Plus Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows  + 1):  # Inner loop for columns
        if i == rows  // 2 + 1 or j == rows  // 2 + 1:  # Print stars in plus pattern
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space
    print()


'''''''''Output:
Enter the row size for the pattern: 5
    *     
    *     
* * * * * 
    *     
    *     

=== Code Execution Successful ==='''

# Code Explanation:
# First, we take the row size input from the user.

# The outer loops handle the rows, the inner loops work on the columns.

# We check if the current row or column is in the middle. If it is, we print a star(“*”).

# This creates a “plus” pattern where the middle row and middle column are filled with stars, and the rest are spaces.