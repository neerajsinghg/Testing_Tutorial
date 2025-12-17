# 14. Find the Factorial of a Number

# Example:

# Factorial of 5 = 5*4*3*2*1 = 120

num = int(input("Enter a number : "))

product = 1

for i in range(1,num+1):
    product = product * i 
    
print(f"The Factorial of the number is {product}")
