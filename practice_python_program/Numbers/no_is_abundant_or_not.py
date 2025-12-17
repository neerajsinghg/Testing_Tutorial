# 2. Check Whether a Number is Abundant Number or not
# A number in which the sum of it’s divisors is greater than the number is known as Abundant Number
# Let’s take number 12 as an example
# Sum of it’s divisors = 1+2+3+4+6 = 16 which is greater than 12. Hence, It is an abundant number

num = int(input("Enter the number : "))
add = 0 
for i in range(1, num):
    if (num%i==0):
        add = add + i
        
if (num<add):
    print(f'{num} is an abundant number')
else:
    print("It is not an abundant number")