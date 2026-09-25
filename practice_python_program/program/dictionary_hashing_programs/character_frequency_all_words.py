"""
Interview Question:
How do you count the overall frequency of all characters across a list of strings using a dictionary?

Interview Explanation:
In automation testing (e.g., analyzing API payloads or text responses), you often need to aggregate character counts across multiple text blocks.
Using Python's `collections.Counter` or a standard dictionary, you iterate through each word and character to build a global frequency map.

Key Concepts:
1. `collections.Counter` handles character counting cleanly.
2. Iterating through a list of strings and updating counts.
3. Case sensitivity handling (e.g., converting all text to lowercase).
"""

from collections import Counter


def count_global_char_frequency(words: list, ignore_spaces: bool = True) -> dict:
    """
    Counts the frequency of each character across all words in a list.
    """
    char_counter = Counter()

    for word in words:
        for char in word.lower():
            if ignore_spaces and char.isspace():
                continue
            char_counter[char] += 1

    return dict(char_counter)


if __name__ == "__main__":
    sample_words = ["Selenium", "Automation", "Pytest Framework"]

    frequency = count_global_char_frequency(sample_words)
    print("Global Character Frequency:")
    for char, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"'{char}': {count}")
