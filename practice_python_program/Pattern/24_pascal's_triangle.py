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
