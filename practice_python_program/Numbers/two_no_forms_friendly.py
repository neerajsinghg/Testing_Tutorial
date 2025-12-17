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
