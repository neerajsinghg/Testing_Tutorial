# num = int(input("enter a no = "))
# flag = False
# if num == 1:
#     print("this is not a prime no ")

# elif num>1:
#     for i in range(2, num):
#         if(num%i)==0:
#             flag = True
#             break

# if flag:
#     print("this is not a prime number")
# else:
#     print("this is a prime num ")

#prime no between 1 to 10

lower = 1
upper = 10

print("prime numvers between ", lower, " and ", upper, "are = ")

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if(num%i) == 0:
                break
        else:
            print(num)