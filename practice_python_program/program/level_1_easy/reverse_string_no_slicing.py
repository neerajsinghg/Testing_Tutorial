"""
2. Reverse a String without Slicing
Interview Note: Iterates through characters and prepends each char to the result string.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string_loop(text: str) -> str:
    result = ""
    for char in text:
        result = char + result
    return result

if __name__ == "__main__":
    text = "selenium"
    print("Original:", text)
    print("Reversed (without slicing):", reverse_string_loop(text))
