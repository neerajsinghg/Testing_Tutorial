#Question 6: Hollow Square Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == 1 or i == rows or j == 1 or j == rows :  # Print star only on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''Output:
Enter the row size for the pattern: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python with a hollow square.

# The outer loop runs through each row, and the inner loop prints stars (*) only on the borders (first/last row or column).

# Inside the square, spaces (" ") are printed to maintain the hollow effect. Using end=" " keeps characters on the same line, while print() moves to the next row of the program.
