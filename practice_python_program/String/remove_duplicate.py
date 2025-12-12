def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

# Example
string = "programming"
print(remove_duplicates(string)) # Output: "progamin"