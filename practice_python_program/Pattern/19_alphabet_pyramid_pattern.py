#Question 19: Alphabet Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for alphabets
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse alphabets
        print(chr(64 + l), end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input, and the outer loop controls the rows of the pattern.

# The first inner loop prints spaces, the second prints alphabets in increasing order, and the third prints the reverse sequence of alphabets.

# chr(64 + k) converts numbers to letters starting from 'A'. This creates a symmetrical alphabet pattern in Python.
