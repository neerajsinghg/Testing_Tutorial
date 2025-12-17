#Question 27: Hollow Square Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == 1 or i == rows or j == 1 or j == rows:  # Print numbers only on borders
            print(j, end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()  # Move to the next line


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 
1       5 
1       5 
1       5 
1 2 3 4 5 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size as input to create a border pattern with numbers.

# The outer loop controls the rows, and the inner loop controls the columns.

# We print numbers only on the borders (first row, last row, first column, and last column), leaving spaces inside. After each row, we move to the next line to complete the pattern.
