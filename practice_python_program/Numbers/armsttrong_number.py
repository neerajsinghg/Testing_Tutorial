# 6. Print the Armstrong Numbers in Nth Range
# An number is an Armstrong number if the sum of its own digits, each raised to the power of n, is equal to the number itself.

# Example:
# 153 = 1³ + 5³ + 3³ = 153
# 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1634

range = int(input("Enter the range : "))

for i in range(1, range):
    add = 0 
    length = len(str(i))
    temp = i 
    while (temp != 0):
        reminder = temp % 10 
        add = add + (reminder**length)
        temp = temp // 10 
    
    if (i==add):
        print(i)
