"""
Count Words Frequency in Sentence
Interview Note: Splits sentence into words and builds frequency dict.
Time Complexity: O(n)
Space Complexity: O(w)
"""

def count_words(text: str) -> dict[str, int]:
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

if __name__ == "__main__":
    text = "python selenium python pytest"
    print("Word Count:", count_words(text))
