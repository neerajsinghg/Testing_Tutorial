"""
Check Palindrome Without Slicing (Two Pointers)
Interview Note: Uses left and right pointers converging inward to avoid creating reversed string copies.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome_two_pointers(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    text = "madam"
    print(f"Is '{text}' palindrome?", is_palindrome_two_pointers(text))
