#Question 20: Inverted Alphabet Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for alphabets
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse alphabets
        print(chr(64 + l), end=" ")
    print()  # Move to the next line


'''''''''Output:
Enter the row size for the pattern: 5
A B C D E D C B A 
  A B C D C B A 
    A B C B A 
      A B A 
        A 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input, and the outer loop runs in reverse to form the pattern.

# The first inner loop prints spaces to align the alphabets, while the second and third loops print alphabets in increasing and decreasing order, respectively, forming a symmetrical pattern.

# This code generates a diamond-like pattern of alphabets, with spaces inside and alphabets on the borders, creating a beautiful shape.
