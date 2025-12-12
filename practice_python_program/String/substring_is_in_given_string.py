# 9. Create a program that checks if a substring is present in a given string.

word = input("Enter a string: ")
sub = input("Enter the substring to check : ")

if sub in word:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")