#Question 17: Alphabet Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(chr(64 + j), end=" ")  # Print alphabets
    print()


'''''''''Output:
Enter the row size for the pattern: 5
A 
A B 
A B C 
A B C D 
A B C D E 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size input and use loops to print alphabets in a pattern. Each row prints the letters starting from 'A' and increasing with each column.

# The chr(64 + j) converts numbers to corresponding uppercase letters. The end=" " ensures the letters stay on the same line, and print() moves to the next row.
