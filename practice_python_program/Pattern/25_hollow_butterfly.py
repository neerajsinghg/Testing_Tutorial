#Question 25: Hollow Butterfly Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Upper part of butterfly
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(rows, 0, -1):  # Lower part of butterfly
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
*                 * 
* *             * * 
*   *         *   * 
*     *     *     * 
*       * *       * 
*       * *       * 
*     *     *     * 
*   *         *   * 
* *             * * 
*                 * 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by inputting the row size to create the butterfly pattern program in Python.

# In the upper part, stars are printed at the start and end of each row, with spaces in between.

# We add spaces between the two halves of the butterfly to form the wings.

# The lower part mirrors the upper part, decreasing the number of stars as we move down, completing the butterfly shape.
