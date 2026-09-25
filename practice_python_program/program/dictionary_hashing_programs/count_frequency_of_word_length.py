"""
Interview Question: How do you group words in a sentence by their character length using a dictionary?

Interview Explanation:
"I split the text into words and use `collections.defaultdict(list)` or `result.setdefault(len(word), []).append(word)`.
This groups words of length 3, 4, 5, etc., into corresponding lists."
"""

from collections import defaultdict

def group_words_by_length(sentence: str) -> dict[int, list[str]]:
    length_map = defaultdict(list)
    for word in sentence.split():
        clean_word = word.strip(".,!?")
        length_map[len(clean_word)].append(clean_word)
    return dict(length_map)

if __name__ == "__main__":
    text = "Python selenium pytest automation testing framework"
    print("Grouped by Word Length:", group_words_by_length(text))
