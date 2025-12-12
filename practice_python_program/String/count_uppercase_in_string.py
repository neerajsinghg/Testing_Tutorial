# 4. Write a program that takes a string as input and counts the number of uppercase letters in the string.

# x = input("Enter a string: ")
x="What is your Good name"
upper=0
lower = 0
for i in x:
    if i.isupper():
        upper += 1
    if i.islower():
        lower +=1
    else:
        pass
print("Upper: ", upper)
print("Lower: ",lower)

