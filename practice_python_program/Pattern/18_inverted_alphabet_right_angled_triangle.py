#Question 18: Inverted Alphabet Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        print(chr(64 + j), end=" ")  # Print alphabets
    print()  # Move to the next line


'''''''''Output:
Enter the row size for the pattern: 5
A B C D E 
A B C D 
A B C 
A B 
A 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size input. The outer loop handles each row in reverse order, while the inner loop prints alphabets in each row.

# chr(64 + j) converts number to corresponding alphabet letters starting from ‘A’.

# end=" " keeps the character on the same line, and prints() moves to the next line, creating a reverse alphabet pattern in Python.
