"""
Interview Question: How do you remove all vowels from a string in Python?

Interview Explanation:
"I iterate through characters in the string and filter out any character present in the set `vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}` using generator join `"".join(char for char in text if char not in vowels)`."
"""

def remove_vowels(text: str) -> str:
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)

if __name__ == "__main__":
    text = "Python Selenium Automation"
    print("Original:", text)
    print("Without Vowels:", remove_vowels(text))
