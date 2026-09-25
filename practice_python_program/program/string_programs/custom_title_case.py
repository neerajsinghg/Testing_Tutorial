"""
Interview Question: How do you capitalize the first letter of each word in a string without using built-in title()?

Interview Explanation:
"I split the string into words using `text.split()`.
For each word, I capitalize the first character `word[0].upper() + word[1:].lower()` and join words with space.
This avoids `title()`'s edge case bug where punctuation causes incorrect capitalization (e.g. `they're` -> `They'Re`)."
"""

def custom_title_case(text: str) -> str:
    words = text.split()
    capitalized = [w[0].upper() + w[1:].lower() if len(w) > 0 else w for w in words]
    return " ".join(capitalized)

if __name__ == "__main__":
    sentence = "python selenium sdet interview questions"
    print("Original:", sentence)
    print("Custom Title Case:", custom_title_case(sentence))
