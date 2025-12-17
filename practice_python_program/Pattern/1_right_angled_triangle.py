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