#Question 9: Hollow Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop handles the rows, while the inner loops handle spaces and stars.

# Stars are printed at the borders of the pyramid, while the inside remains empty except for the bottom row.

# This creates a hollow pyramid shape with stars on the edges, and spaces inside the pyramid.
