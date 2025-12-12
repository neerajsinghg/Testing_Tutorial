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