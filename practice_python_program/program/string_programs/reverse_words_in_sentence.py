"""
Reverse Words in a Sentence
Interview Note: Splits sentence into words, reverses the word list, and joins with space.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])

if __name__ == "__main__":
    text = "Python Selenium Automation"
    print("Original:", text)
    print("Reversed words:", reverse_words(text))
