# 1. Find the Sum of the First N Natural Numbers

# Given a Natural Number of N, we need to find the sum of all the natural numbers until the value of N. We can use different methods to write the Python code and one of the most effective method is using For Loop.
range = int(input("Enter the ranges: "))
add = 0
for  i in range(range+1):
     add = add + i 

print(f"The sum of the first {range} numbers is {add}")

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

# 3. Check Whether a Number is Automorphic Number or Not
# A Number is known as an Automorphic Number if the last digits of it’s square is same as the number itself
# Let’s take number 76 as an example
# 76² = 5776
# The last two digit of the square , 76 is equal to the number itself

num = int(input("Enter a number : "))
length = len(str(num))
sqr = str(num ** 2)
print(sqr)

new = int(sqr[(length):])
print(new)

if (new == num):
    print("It is an Automorphic Number")
else:
    print("It is not an Automorphic Number")

# 4. Print N number of Automorphic numbers in a given range
# A Range N will be given and we need to print all the automorphic numbers up to that range. To Know more about Automorphic Number, Refer To Question 4.

range = int(input('Enter the given range : '))

for i in range(1, range):
    sqr = i**2
    mod = 10 ** len(str(i))
    if (sqr%mod == i):
        print(i)

# 5. Print Harshad Numbers in nth range
# A number that is divisible by sum of it’s own digits is know an Harshad Number.
# Example: 12 , 1+ 2 = 3 , 12 is divisible by 3

range = int(input("Enter the range : "))

for i in range(1, range):
    add = 0 #Use Flag Equations in Outer Loop 
    for j in str(i):
        add = add + int(j)
    if (i %add == 0):
        print(i)

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

# 7. Check Whether a Number is Palindrome or Not
# A number when reversed, equates to the same number is known as Palindrome Number
# 121 reversed is 121 itself


num = int(input("Enter a number: "))

temp = num
new = 0 
while (temp!=0):
    reminder = temp % 10 
    new = (new * 10) + reminder
    temp = temp // 10
    
print(new)

if (num == new):
    print("The Number is Palindrome")
else:
    print("The Number is not a palindrome")

# 8. Print the Reverse of a Number

num = int(input("Enter a number: "))

temp = num
new = 0 
while (temp!=0):
    reminder = temp % 10 
    new = (new * 10) + reminder
    temp = temp // 10
    
print(new)

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

# 10. Greatest Of Three Numbers
n1, n2, n3 = map(int, input("Enter Three Numbers : ").split())

if (n1>=n2) and (n1>=n3):
    print(f'{n1} is the greatest')
elif (n2>=n1) and (n2>=n3):
    print(f'{n2} is the greatest')
elif (n3>=n1) and (n3>=n2):
    print(f'{n3} is the greatest')
else:
    print("They are all Equal")

# 11. Print Abundant Numbers in The range N
# Numbers upto the range N is checked whether it is an abundant number or not. For more reference , Check Problem Number 3
# A number that is smaller than the sum of all its factors except the number itself is known as an abundant number 

num = int(input("Enter the number : "))
add = 0 
for i in range(1, num):
    if (num%i==0):
        add = add + i
        
if (num<add):
    print(f'{num} is an abundant number')
else:
    print("It is not an abundant number")

# 11. Check whether a Year is Leap Year or Not.
# Conditions for a Leap Year :
# The year should be perfectly divisible by 400.
# The year divisible by 4 but not by 100.

year = int(input("Enter a Year  :"))

if (year%4==0 and year%100 !=0) or (year%400 == 0):
    print("Leap Year")
else:
    print("No Leap Year")

# 12. Checking Whether a number is prime or not
# Prime Number is a number which is divisible by 1 and the number itself

num = int(input("Enter a number : "))

flag = 0
if (num>1):
    for i in range(2, num):
        if (num%i==0):
            flag = 1 
            break;
    if flag == 1:
        print("Composite Number")
    else:
        print("Prime Number")
    
else:
    print("Neither Prime Nor Composite")

# 13.Print the Prime Numbers in a Given Range

range = int(input("Enter the range you want: "))

for i in range(2, range):
    flag = 0 #Used To Assume a number is prime , on every new outerloop , the value is resetted to 0 
    for j in range(2, i):
        if (i%j==0):
            flag  = 1
            break
    if (flag ==0):
        print(i)

# 14. Find the Factorial of a Number

# Example:

# Factorial of 5 = 5*4*3*2*1 = 120

num = int(input("Enter a number : "))

product = 1

for i in range(1,num+1):
    product = product * i 
    
print(f"The Factorial of the number is {product}")

# 15. Find the Power Of a Number using Iteration (Most Basic)

num, power = map(int, input("Enter the num and the power : ").split())

#print(num ** power)

# Using Simple Iteration 

output = 1 
for i in range(power):
    output = output * num 
    
print(output)

# 16. Check whether a number is Perfect Number or Not
# A perfect number is a number whose sum of it’s divisors is equal to the number itself.
# For example, 28
# Sum of it’s divisors = 1 + 14 + 2 + 4 + 7 = 28 which is equal to the number itself

num = int(input("Enter a number : "))
add = 0

for i in range(1, num):
    if num % i == 0:
        add = add + i

if (num == add):
    print("Perfect Number")
else:
    print("Not Perfect Number")

# 17. Find the Prime Factors of a Given Number:
# Factors of a Number which is only divisible by 1 and the number itself is known as Prime Factors


n = int(input("Enter the number : "))
arr = []
for i in range(2, n):
    if n % i == 0:
        arr.append(i)
print(arr)
sol = []

for j in arr:
    flag = 0
    for k in range(2, j):
        if j % k == 0:
            flag = 1 
            break 
    if flag == 0:
        sol.append(j)

print("The Prime Factors of the number are: ")
for m in sol:
    print(m, end=' ')

# 18. Find whether a number is perfect square or not

# Examples of Perfect Number : 4, 9, 16, 25 etc

import math 
num = int(input("Enter the number : "))
result1 = int(math.sqrt(num))
if float(result1) == math.sqrt(num):
    print("Yes")
else:
    print("No")

# 19. Check Whether Two Numbers forms a friendly pair or not
# Read Two Numbers
# Find The Factors of Both The Numbers
# Divide the sum of the factors with the number for each of these numbers
# If the resultant of the above step for each numbers are same, then both of these numbers are said to be friendly pairs.

num1, num2 = map(int, input("Enter the two numbers : ").split())

sum1 = 0 
sum2 = 0 
for i in range(1, num1+1):
    if num1 % i == 0:
        sum1 = sum1 + i

for j in range(1, num2+1):
    if num2 % j == 0:
        sum2 = sum2 + j

result1 = sum1 / num1
result2 = sum2 / num2 

if (result1==result2):
    print(f"{num1} and {num2} are friendly pairs")
else:
    print("They are not friendly pairs")

# 20. Check Whether or Not the Number is a Strong Number
# A Number whose sum of the factorials of it’s digits is equal to the number itself is known as Strong Number
# For Example :
# 145;
# 1!+4!+5! = 145; Hence it is a strong number.

n = int(input("Enter a number : "))

digits = []
for i in str(n):
    digits.append(int(i))
add = 0  
for i in digits:
    product = 1
    for j in range(1, i+1):
        product = product * j
    add = add + product
print(add)
if (n==add):
    print("It is a strong number")
else:
    print("It is not a strong number")