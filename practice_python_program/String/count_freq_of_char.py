### 5. **Count Character Frequency**
#**Problem**: Write a program to count the frequency of each character in a string.

from collections import Counter

def char_frequency(s):
    return dict(Counter(s))


# Example
string = "hello"
print(char_frequency(string)) # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}