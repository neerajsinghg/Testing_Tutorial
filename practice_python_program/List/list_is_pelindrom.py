# 32. Write a Python program to check if a list is a palindrome.

palindrome_list = [1, 2, 3, 2, 1]

if palindrome_list==palindrome_list[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")