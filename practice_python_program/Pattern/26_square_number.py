#Question 26: Square Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

=== Code Execution Successful ==='''

# Code Explanation: 
# We start by taking the row size as input to create a number pattern.

# In each row, we print numbers from 1 to the row using a nested loop. The outer loop controls the rows, and the inner loop controls the printing of numbers. After each row, we move to the next line to complete the pattern.
