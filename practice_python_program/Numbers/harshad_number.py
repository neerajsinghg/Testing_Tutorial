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