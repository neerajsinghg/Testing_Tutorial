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