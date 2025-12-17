#Question 21: Alphabet Diamond Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Upper part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):
        print(chr(64 + l), end=" ")
    print()
for i in range(rows - 1, 0, -1):  # Lower part of diamond
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):
        print(chr(64 + l), end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 
  A B C D C B A 
    A B C B A 
      A B A 
        A 

=== Code Execution Successful ==='''

# Code Explanation:
# We begin by taking the number of rows as input for the pattern in Python.

# The first loop handles the upper part of the diamond by printing spaces and then alphabets in increasing order, followed by a decreasing order.

# We then repeat the process for the lower part of the diamond in reverse to complete the pattern.

# This pattern in Python creates a diamond shape with alphabets arranged symmetrically. It uses loops for controlling spaces and alphabet printing.
