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
