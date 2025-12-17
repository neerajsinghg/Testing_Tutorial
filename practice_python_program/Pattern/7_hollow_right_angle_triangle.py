#Question 7: Hollow Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        if j == 1 or i == rows or i == j:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''Output:
Enter the row size for the pattern: 5
* 
* * 
*   * 
*     * 
* * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop controls the rows, while the inner loop prints stars and spaces.

# Stars are printed on the left, right, and bottom edges of the triangle, while spaces fill the inside. This forms a right-angled hollow triangle. print() moves to the next row, keeping the pattern structured.
