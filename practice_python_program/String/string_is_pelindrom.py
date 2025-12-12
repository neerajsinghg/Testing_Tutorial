# 8. Create a program that checks if a given string is a palindrome.
word = input("Enter the string: ")

if word.replace(" ","").lower() == word[::-1].replace(" ","").lower():
    print("The given string is paliandrome")
else:
    print("The given string is not paliandrome")

### 2. **Check for Palindrome**
#**Problem**: Write a program to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

# Example
string = "madam"
print(is_palindrome(string)) # Output: True