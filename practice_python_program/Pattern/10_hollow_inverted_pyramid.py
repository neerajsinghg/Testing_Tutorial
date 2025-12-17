#Question 10: Hollow Inverted Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''''''''Output:
Enter the row size for the pattern: 5
* * * * * * * * * 
  *           * 
    *       * 
      *   * 
        * 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size input, and the outer loop runs in reverse to create the pattern.

# The first inner loop prints spaces to align the star, while the second prints stars on the borders, leaving spaces in the middle except for the last row.

# The if condition ensures stars are printed on the borders and at the ends of each row, creating a hollow pattern with stars in Python.
