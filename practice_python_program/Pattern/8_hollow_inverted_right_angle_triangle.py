#Question 8: Hollow Inverted Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(rows , 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        if j == 1 or i == rows or i == j:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()  # Move to the next line


'''Output:
Enter the row size for the pattern: 4
* * * * 
*   * 
* * 
* 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop handles the row, and the inner loop prints the stars and spaces.

# Stars are placed on the left, right and diagonal edges, while the inside remains empty. This creates a hollow inverted right-angled triangle. The print() function ensures the proper row format.
