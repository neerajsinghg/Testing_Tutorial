#Question 12: Number Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 
1 2 
1 2 3 
1 2 3 4 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a number pattern in Python.

# The outer loop controls the rows, and the inner loop prints numbers from 1 to the current row number. Each row increases the range of numbers printed, forming a simple number pattern.
