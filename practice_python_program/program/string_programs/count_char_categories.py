"""
Interview Question: How do you count uppercase letters, lowercase letters, digits, and special characters in a string?

Interview Explanation:
"I iterate through each character in the string and inspect built-in str methods: `char.isupper()`, `char.islower()`, and `char.isdigit()`.
If none match, I count it as a special character."
"""

def count_categories(text: str) -> dict[str, int]:
    counts = {"uppercase": 0, "lowercase": 0, "digits": 0, "special": 0}
    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1
    return counts

if __name__ == "__main__":
    sample_str = "Python 3.10 @ Selenium!"
    print("Sample:", sample_str)
    print("Category Counts:", count_categories(sample_str))
