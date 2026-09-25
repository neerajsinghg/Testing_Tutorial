"""
Interview Question: How do you check if a string is a valid palindrome while ignoring spaces, punctuation, and case?

Interview Explanation:
"I first filter out non-alphanumeric characters using `char.isalnum()` and convert characters to lowercase.
Then I check if the cleaned string equals its reverse `cleaned == cleaned[::-1]` (or use two-pointer technique)."
"""

def is_valid_palindrome(text: str) -> bool:
    cleaned = [char.lower() for char in text if char.isalnum()]
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    sentence1 = "A man, a plan, a canal: Panama"
    sentence2 = "race a car"
    print(f"'{sentence1}' valid palindrome?", is_valid_palindrome(sentence1))
    print(f"'{sentence2}' valid palindrome?", is_valid_palindrome(sentence2))
