#Question 1: Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print("*", end=" ")   # Print star
    print()


'''Output:
Enter the row size for the pattern: 5
* 
* * 
* * * 
* * * * 
* * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a star pattern.

# The outer loop runs through each row, while the inner loop prints stars equal to the row number.

# Using end=" " keeps stars on the same line, and print() moves to the next row.

#Question 2: Inverted Right-Angled Triangle in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        print("*", end=" ")   # Print star
    print()


'''Output:
Enter the row size for the pattern: 5
* * * * * 
* * * * 
* * * 
* * 
* 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a reverse star pattern.

# The outer loop starts from the given row size and decreases, while the inner loop prints stars equal to the row number.

# Using end=" " keeps stars on the same line, and print() moves to the next row.

#Question 3: Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()


'''Output:
Enter the row size for the pattern: 5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the row size and use loops to print a pyramid pattern. The first inner loop adds spaces for alignment, and the second loop prints stars in an increasing order.

# This approach creates a pattern program in Python, where each row has centered stars forming a triangle shape.

#Question 4: Inverted Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows , 0, -1):  # Outer loop for rows in reverse
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()  # Move to the next line


'''Output:
Enter the row size for the pattern: 5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take user input for rows and use loops to create an inverted pyramid pattern.

# The first inner loop prints spaces to align stars properly, while the second prints stars in decreasing order.

# This simple pattern in Python helps us learn loops and alignment, making it easy to create different star shapes.

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

#Question 6: Hollow Square Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == 1 or i == rows or j == 1 or j == rows :  # Print star only on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''Output:
Enter the row size for the pattern: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python with a hollow square.

# The outer loop runs through each row, and the inner loop prints stars (*) only on the borders (first/last row or column).

# Inside the square, spaces (" ") are printed to maintain the hollow effect. Using end=" " keeps characters on the same line, while print() moves to the next row of the program.

#Question 7: Hollow Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        if j == 1 or i == rows or i == j:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()

'''Output:
Enter the row size for the pattern: 5
* 
* * 
*   * 
*     * 
* * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop controls the rows, while the inner loop prints stars and spaces.

# Stars are printed on the left, right, and bottom edges of the triangle, while spaces fill the inside. This forms a right-angled hollow triangle. print() moves to the next row, keeping the pattern structured.

#Question 8: Hollow Inverted Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(rows , 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        if j == 1 or i == rows or i == j:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()  # Move to the next line


'''Output:
Enter the row size for the pattern: 4
* * * * 
*   * 
* * 
* 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop handles the row, and the inner loop prints the stars and spaces.

# Stars are placed on the left, right and diagonal edges, while the inside remains empty. This creates a hollow inverted right-angled triangle. The print() function ensures the proper row format.

#Question 9: Hollow Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * * 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a pattern in Python. The outer loop handles the rows, while the inner loops handle spaces and stars.

# Stars are printed at the borders of the pyramid, while the inside remains empty except for the bottom row.

# This creates a hollow pyramid shape with stars on the edges, and spaces inside the pyramid.

#Question 10: Hollow Inverted Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()


'''''''''Output:
Enter the row size for the pattern: 5
* * * * * * * * * 
  *           * 
    *       * 
      *   * 
        * 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size input, and the outer loop runs in reverse to create the pattern.

# The first inner loop prints spaces to align the star, while the second prints stars on the borders, leaving spaces in the middle except for the last row.

# The if condition ensures stars are printed on the borders and at the ends of each row, creating a hollow pattern with stars in Python.

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

#Question 12: Number Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 
1 2 
1 2 3 
1 2 3 4 

=== Code Execution Successful ==='''

# Code Explanation:
# We take input for the number of rows to create a number pattern in Python.

# The outer loop controls the rows, and the inner loop prints numbers from 1 to the current row number. Each row increases the range of numbers printed, forming a simple number pattern.

#Question 13: Inverted Number Right-Angled Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input. The outer loop runs in reverse order, starting from the row size down to 1.

# In each row, the inner loop prints from 1 up to the current row number. After each row, print() move to the next line.

#Question 14: Number Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for numbers
        print(k, end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
        print(l, end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input and use a loop to print rows. The first inner loop adds spaces to center the numbers.

# The second inner loop prints numbers from 1 to the current row number. The third inner loop prints the reverse numbers.

# This creates a pattern where numbers increase from 1 to the row number and then decrease, with spaces to center them.

#Question 15: Inverted Number Pyramid Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, i + 1):  # Inner loop for numbers
        print(k, end=" ")
    for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
        print(l, end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 4 3 2 1 
  1 2 3 4 3 2 1 
    1 2 3 2 1 
      1 2 1 
        1 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size input and run loops to print the pattern in reverse order, starting from the largest row.

# The first inner loop prints spaces for proper alignment. Then, the second loop prints numbers in increasing order, while the third loop prints the same numbers in reverse.

# Each row is printed using print(), creating a symmetric pattern of numbers with spaces in between.

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

#Question 22: Floyd's Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
num = 1
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(num, end=" ")  # Print numbers in sequence
        num += 1
    print()


'''''''''Output:
Enter the row size for the pattern: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the number of rows as input for the pattern and initialize num to 1.

# The outer loop runs for each row, and the inner loop prints numbers in sequence, increasing with each iteration. The number increases after each point, and we use print() to move to the next line after each row is completed.

#Question 23: Pascal's Triangle Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows ):  # Outer loop for rows
    num = 1
    for j in range(rows - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(i + 1):  # Inner loop for numbers
        print(num, end="   ")
        num = num * (i - k) // (k + 1)  # Calculate Pascal's number
    print()


'''''''''Output:
Enter the row size for the pattern: 5
          1   
        1   1   
      1   2   1   
    1   3   3   1   
  1   4   6   4   1   

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input to create the pattern.

# The outer loop runs for each row, and in each row, we first print spaces for alignment. Then, the inner loop prints the Pascal's Triangle numbers. We calculate these numbers using the formula num = num * (i - k) // (k + 1).

# After each row, we move to the next line using print().

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

#Question 26: Square Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

=== Code Execution Successful ==='''

# Code Explanation: 
# We start by taking the row size as input to create a number pattern.

# In each row, we print numbers from 1 to the row using a nested loop. The outer loop controls the rows, and the inner loop controls the printing of numbers. After each row, we move to the next line to complete the pattern.

#Question 27: Hollow Square Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == 1 or i == rows or j == 1 or j == rows:  # Print numbers only on borders
            print(j, end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()  # Move to the next line


'''''''''Output:
Enter the row size for the pattern: 5
1 2 3 4 5 
1       5 
1       5 
1       5 
1 2 3 4 5 

=== Code Execution Successful ==='''

# Code Explanation:
# We start by taking the row size as input to create a border pattern with numbers.

# The outer loop controls the rows, and the inner loop controls the columns.

# We print numbers only on the borders (first row, last row, first column, and last column), leaving spaces inside. After each row, we move to the next line to complete the pattern.

#Question 28: Zig-Zag Number Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if (i + j) % 2 == 0:  # Print numbers in zig-zag pattern
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


'''''''''Output:
Enter the row size for the pattern: 4
1 0 1 0 
0 1 0 1 
1 0 1 0 
0 1 0 1 

=== Code Execution Successful ==='''

# Code Explanation:
# We take the row size as input to create a zig-zag pattern with numbers.

# The outer loop handles the rows, while the inner loop controls the columns.

# We check if the sum of the row and column indices is even. If so, we print "1"; otherwise, we print "0".

# This creates an alternating pattern of "1"s and "0"s in a zig-zag format across the grid.

#Question 29: Cross Pattern in Python

rows = int(input("Enter the row size for the pattern:"))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == j or i + j == rows + 1:  # Print stars in cross pattern
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space
    print()


'''''''''Output:
Enter the row size for the pattern: 5
*       * 
  *   *   
    *     
  *   *   
*       * 

=== Code Execution Successful ==='''

# Code Explanation: 
# We start by taking the row input for the pattern.

# The outer loop controls the rows, and the inner loop handles the columns.

# We check two conditions: if the row number equals the column number, or if their sum equals the total rows plus one. If either is true, we print a star(“*”).

# This creates a cross pattern with stars in the grid, with spaces in other positions.

#Question 30: Plus Pattern in Python

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows  + 1):  # Inner loop for columns
        if i == rows  // 2 + 1 or j == rows  // 2 + 1:  # Print stars in plus pattern
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space
    print()


'''''''''Output:
Enter the row size for the pattern: 5
    *     
    *     
* * * * * 
    *     
    *     

=== Code Execution Successful ==='''

# Code Explanation:
# First, we take the row size input from the user.

# The outer loops handle the rows, the inner loops work on the columns.

# We check if the current row or column is in the middle. If it is, we print a star(“*”).

# This creates a “plus” pattern where the middle row and middle column are filled with stars, and the rest are spaces.