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