### 9. **Replace a Substring**
#**Problem**: Write a program to replace all occurrences of a substring in a string.

def replace_substring(s, old, new):
    return s.replace(old, new)

# Example
string = "hello world"
print(replace_substring(string, "world", "there")) # Output: "hello there"