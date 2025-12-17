#Question 11: Hollow Diamond Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Upper part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()
for i in range(rows - 1, 0, -1):  # Lower part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''Output:
Enter the row size for the pattern: 5
        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking input for the number of rows to create a diamond pattern in Python.

# The upper part of the diamond is created first, printing stars at the borders and leaving spaces inside.

# Then, we move to the lower part of the diamond, following the same pattern with stars at the borders.

# This approach creates a hollow diamond shape with stars on the edges and spaces inside, forming a symmetrical pattern.
