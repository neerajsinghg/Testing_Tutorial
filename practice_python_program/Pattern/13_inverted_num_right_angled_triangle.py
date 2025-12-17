#Question 13: Inverted Number Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input. The outer loop runs in reverse order, starting from the row size down to 1.

# In each row, the inner loop prints from 1 up to the current row number. After each row, print() move to the next line.
