# 9. Find the Sum of the digits of a number

# Each digit of a number is taken and added to get the required result
num = int(input("Enter a number : "))

# Let us Do This By using modulus
add = 0 

while (num!=0):
    reminder = num % 10
    add = add + reminder 
    num = num // 10
    
print(add)