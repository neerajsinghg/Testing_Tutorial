#Question 15: Inverted Number Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for numbers
        print(k, end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
        print(l, end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 4 3 2 1 
  1 2 3 4 3 2 1 
    1 2 3 2 1 
      1 2 1 
        1 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size input and run loops to print the pattern in reverse order, starting from the largest row.

# The first inner loop prints spaces for proper alignment. Then, the second loop prints numbers in increasing order, while the third loop prints the same numbers in reverse.

# Each row is printed using print(), creating a symmetric pattern of numbers with spaces in between.
