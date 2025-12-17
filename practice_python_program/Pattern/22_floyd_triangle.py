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
