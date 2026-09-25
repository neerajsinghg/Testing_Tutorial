"""
24. Find Frequency of Words in a Sentence
Interview Note: Splits sentence into tokens and counts word occurrences using dict.
Time Complexity: O(n)
Space Complexity: O(w) where w is number of unique words.
"""

def word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    text = "python selenium python pytest selenium python"
    print("Word Frequencies:", word_frequency(text))
