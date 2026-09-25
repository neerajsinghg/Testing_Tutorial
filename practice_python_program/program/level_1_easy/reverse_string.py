"""
1. Reverse a String using Slicing
Interview Note: String slicing [::-1] creates a reversed copy.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(text: str) -> str:
    return text[::-1]

if __name__ == "__main__":
    text = "selenium"
    print("Original:", text)
    print("Reversed:", reverse_string(text))
