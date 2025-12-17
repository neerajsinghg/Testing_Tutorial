# 4. Print N number of Automorphic numbers in a given range
# A Range N will be given and we need to print all the automorphic numbers up to that range. To Know more about Automorphic Number, Refer To Question 4.

range = int(input('Enter the given range : '))

for i in range(1, range):
    sqr = i**2
    mod = 10 ** len(str(i))
    if (sqr%mod == i):
        print(i)
