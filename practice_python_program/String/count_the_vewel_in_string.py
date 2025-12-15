# 12. Write a program that counts the number of vowels in a given string.

word = input("Enter a text : ")

vowels='AEIOUaeiou'
x=0
count = len([char for char in word if char in vowels ])
print(count)

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