"""
Reverse String Using Recursion
Interview Note: Base case empty string returns "", recursive step reverse_string(text[1:]) + text[0].
Time Complexity: O(n^2) due to string slicing.
Space Complexity: O(n)
"""

def reverse_string_recursive(text: str) -> str:
    if text == "":
        return ""
    return reverse_string_recursive(text[1:]) + text[0]

if __name__ == "__main__":
    text = "Python"
    print("Original:", text)
    print("Reversed (Recursive):", reverse_string_recursive(text))
