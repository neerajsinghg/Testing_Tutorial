#Question 24: Butterfly Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Upper part of butterfly
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(rows, 0, -1):  # Lower part of butterfly
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

=== Code Execution Successful ==='''

# Code Explanation:
# We first take the row size as input to form the butterfly pattern.

# The outer loops are divided into two parts: the upper and lower parts. In both, we print stars on both sides with spaces in between to create the wings.

# The number of stars decreases as we move down in the lower part of the butterfly, forming the desired shape as per the program.
