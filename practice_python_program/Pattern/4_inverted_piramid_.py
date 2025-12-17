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
