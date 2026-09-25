"""
Reverse Each Word in a Sentence
Interview Note: Splits words and reverses each word individually using slicing while maintaining word order.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_each_word(text: str) -> str:
    return " ".join(word[::-1] for word in text.split())

if __name__ == "__main__":
    text = "Python Selenium"
    print("Original:", text)
    print("Reversed each word:", reverse_each_word(text))
