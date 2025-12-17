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