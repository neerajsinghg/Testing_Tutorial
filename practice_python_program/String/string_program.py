# Write a program that takes two numbers as input and prints their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is : ", num1+num2)

# 2. Write a program that takes a string as input and prints its length.
text = input("Enter a string: ")
print('The length of the entered string is : ', len(text))

# 3. Write a program that takes a sentence and then prints the number of words in that sentence.
sentence = input("Enter a sentence: ")
print("Number of words in the sentence: ",sentence.count(' ')+1)

# 4. Write a program that takes a string as input and counts the number of uppercase letters in the string.
x = input("Enter a string: ")
upper=0
lower = 0
for i in x:
    if i.isupper():
        upper += 1
    if i.islower():
        lower +=1
print("Upper: ", upper)
print("Lower: ",lower)
# 5. Write a program that takes a sentence and then converts all the characters to uppercase.
sentence = input("Enter a sentence: ")
print(sentence.upper())

# 6. Write a program that takes a string as input and replaces all occurrences of the letter ‘a’ with the letter ‘e’.
word = input("Enter a string: ")
rep = word.replace('a','e')
print(rep)

# 7. Create a program that checks if two given strings are anagrams of each other.

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if sorted(word1.replace(" ","").lower()) == sorted(word2.replace(" ","").lower()):
    print("The given words are anagrams")
else:
    print("The given words are not anagrams")

# 8. Create a program that checks if a given string is a palindrome.
word = input("Enter the string: ")

if word.replace(" ","").lower() == word[::-1].replace(" ","").lower():
    print("The given string is paliandrome")
else:
    print("The given string is not paliandrome")

# 9. Create a program that checks if a substring is present in a given string.

word = input("Enter a string: ")
sub = input("Enter the substring to check : ")

if sub in word:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")

# 10. Write a program that reverses the order of words in a given sentence.

sentence = input("Enter a sentence: ")

words = sentence.split(" ")
words.reverse()
newsent=""

for i in words:
    newsent += i + " "
print(newsent)

# 11. Implement a Caesar cipher encryption and decryption program. the key (shift) value of this message is 3.
# The formula of encryption is: En (x) = (x + n) mod 26

message = input("Enter the message")
result = ""
shift =3
for char in message:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    else:
        result += char
print(result)      
# 12. Write a program that counts the number of vowels in a given string.

word = input("Enter a text : ")

vowels='AEIOUaeiou'
x=0
count = len([char for char in word if char in vowels ])
print(count)

# 13. Create a program that converts a given sentence into Pig Latin (move the first letter of each word to the end and add “ay”).

txt = input("Enter a sentence: ")

words = txt.split(" ")
newsent = ""
for i in words:
    newsent += (i[1:]+ i[:1]+"ay ")
print(newsent)

# 14. Write a program that capitalizes the first letter of each sentence in a given paragraph.
paragraph = input("Enter a paragraph: ")
sentences = paragraph.split('.')
output=""
for sent in sentences:    
    cap = sent.strip().capitalize()
    output += cap +'. '
print(output)

# 15. Write a program that finds the longest word in a given sentence.

sentence = input("Enter the sentence: ")
words = sentence.split()
output = max(words, key=len)

print("Longest word in the given sentence:", output)

# 16. Write a program that reverses the order of words in a given sentence.
sentence = input("Enter a sentence :")
words = sentence.split()
words.reverse()
rev = " ".join(words)
print(rev)

# 17. Given a list of strings, write a program to find all pairs of strings that are palindromes.

strings = ["race", "car", "rat", "tar","rac"]

rev=[]
for i in strings:
    if i[::-1] in strings:
        if i not in rev:
            rev.append(i[::-1])
            print(i," and ",i[::-1]," are paliandromes")

# 18. Given three strings, write a program to check if the third string can be formed by interleaving the characters of the first two strings.
s1 = "blue"
s2 = "berry"
s3 = "bbeluerry"

if sorted(s3) == sorted(s1+s2):
    print("The third word is interleaving the characters of the first two words. ")
else:
    print("The third word is not interleaving the characters of the first two words. ")

# 19. Write a program to find all permutations of a smaller string within a larger string.
from itertools import permutations

s = "cbabcacab"
sub = "abc"
sub_permutations = [''.join(p) for p in permutations(sub)]
result =  [p for p in sub_permutations if p in s]
print(result)

# 20. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.
string = "aabcccccaaa"
c=0
new_string = ""
for i,letter in enumerate(string): 
    if letter==string[i-1]:
        c+=1
        if(i+1)==len(string):
            new_string += string[i]+str(c+1)
    else:   
        new_string += string[i-1]+str(c+1)           
        c=0        
print(new_string)











### 1. **Reverse a String**
#**Problem**: Write a program to reverse a string.

def reverse_string(s):
    return s[::-1]

# Example
string = "hello"
print(reverse_string(string)) # Output: "olleh"


### 2. **Check for Palindrome**
#**Problem**: Write a program to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

# Example
string = "madam"
print(is_palindrome(string)) # Output: True


### 3. **Count Vowels and Consonants**
#**Problem**: Write a program to count the number of vowels and consonants in a string.

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

# Example
string = "hello"
vowels, consonants = count_vowels_consonants(string)
print(f"Vowels: {vowels}, Consonants: {consonants}") # Output: "Vowels: 2, Consonants: 3"


### 4. **Remove Duplicates**
#**Problem**: Write a program to remove duplicate characters from a string.

def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

# Example
string = "programming"
print(remove_duplicates(string)) # Output: "progamin"


### 5. **Count Character Frequency**
#**Problem**: Write a program to count the frequency of each character in a string.

from collections import Counter

def char_frequency(s):
    return dict(Counter(s))


# Example
string = "hello"
print(char_frequency(string)) # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


### 6. **Check if Two Strings are Anagrams**
#**Problem**: Write a program to check if two strings are anagrams.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2)) # Output: True


### 7. **Find the Longest Word in a Sentence**
#**Problem**: Write a program to find the longest word in a sentence.

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
sentence = "I love programming in Python"
print(longest_word(sentence)) # Output: "programming"


### 8. **Capitalize the First and Last Character of Each Word**
#**Problem**: Write a program to capitalize the first and last character of each word in a string.

def capitalize_first_last(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > 1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            word = word.upper()
            result.append(word)
    return " ".join(result)

# Example
string = "hello world"
print(capitalize_first_last(string)) # Output: "HellO WorlD"


### 9. **Replace a Substring**
#**Problem**: Write a program to replace all occurrences of a substring in a string.

def replace_substring(s, old, new):
    return s.replace(old, new)

# Example
string = "hello world"
print(replace_substring(string, "world", "there")) # Output: "hello there"


### 10. **Find All Substrings**
#**Problem**: Write a program to find all possible substrings of a string.

def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# Example
string = "abc"
print(all_substrings(string)) # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']