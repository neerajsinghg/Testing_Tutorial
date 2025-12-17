#Question 3: Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()


'''Output:
Enter the row size for the pattern: 5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the row size and use loops to print a pyramid pattern. The first inner loop adds spaces for alignment, and the second loop prints stars in an increasing order.

# This approach creates a pattern program in Python, where each row has centered stars forming a triangle shape.
