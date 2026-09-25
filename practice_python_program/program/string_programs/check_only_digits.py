"""
Check Whether String Contains Only Digits
Interview Note: Uses str.isdigit() for input validation (e.g. form fields, numeric assertions).
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_only_digits(text: str) -> bool:
    return text.isdigit()

if __name__ == "__main__":
    text1 = "123456"
    text2 = "123a56"
    print(f"'{text1}' only digits?", is_only_digits(text1))
    print(f"'{text2}' only digits?", is_only_digits(text2))
