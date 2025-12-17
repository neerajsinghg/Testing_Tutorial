#Question 16: Number Diamond Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Upper part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    print()
for i in range(rows - 1, 0, -1):  # Lower part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 4
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 
  1 2 3 2 1 
    1 2 1 
      1 

=== Code Execution Successful ==='''

# Code Explanation:
# We first take the row size input and use loops to print the upper part of the diamond. Each row consists of spaces, increasing numbers, and reverse numbers.

# The lower part of the diamond is created using similar loops but in reverse order, starting from one less than the row size.

# The loops are designed to ensure proper alignment, creating a symmetric diamond pattern with numbers on both sides and spaces in between.
