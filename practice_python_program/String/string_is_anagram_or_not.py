# 7. Create a program that checks if two given strings are anagrams of each other.

word1 = "what is your good name" #input("Enter the first word: ")
word2 = "what si your good name" #input("Enter the second word: ")

if sorted(word1.replace(" ","").lower()) == sorted(word2.replace(" ","").lower()):
    print("The given words are anagrams")
else:
    print("The given words are not anagrams")

### 6. **Check if Two Strings are Anagrams**
#**Problem**: Write a program to check if two strings are anagrams.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2)) # Output: True