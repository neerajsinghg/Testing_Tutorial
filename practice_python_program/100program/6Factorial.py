num = int(input("enter a num = "))
fact=1
if num<1:
    print("factorial does not exist for a negative number ")
elif num==0:
    print("factorial of 0 is 1 ")
elif num>1:
    for i in range(1, num+1):
        fact = fact*i
    print(fact)