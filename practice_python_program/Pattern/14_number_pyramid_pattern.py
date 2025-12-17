#Question 14: Number Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for numbers
        print(k, end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
        print(l, end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input and use a loop to print rows. The first inner loop adds spaces to center the numbers.

# The second inner loop prints numbers from 1 to the current row number. The third inner loop prints the reverse numbers.

# This creates a pattern where numbers increase from 1 to the row number and then decrease, with spaces to center them.
