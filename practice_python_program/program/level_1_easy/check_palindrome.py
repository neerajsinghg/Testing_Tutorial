"""
3. Check Palindrome
Interview Note: Checks if a string reads the same backwards and forwards.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_palindrome(text: str) -> bool:
    return text == text[::-1]

if __name__ == "__main__":
    test_word = "madam"
    if is_palindrome(test_word):
        print(f"'{test_word}' is a Palindrome")
    else:
        print(f"'{test_word}' is Not palindrome")
