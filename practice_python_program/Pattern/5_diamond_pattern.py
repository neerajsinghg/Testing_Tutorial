#Question 5: Diamond Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1,rows + 1):  # Upper part of diamond
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
for i in range(rows  - 1, 0, -1):  # Lower part of diamond
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()


'''Output:
Enter the row size for the pattern: 4
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 

=== Code Execution Successful ==='''

# Code Explanation:
# We create a diamond pattern in Python using loops. The first loop prints the upper part, increasing stars in each row, while the second loop prints the lower part, decreasing stars row by row.

# Spaces before stars help in alignment, making the diamond shape symmetrical.