"""
Interview Question: How do you group anagrams together from a list of strings in Python?

Interview Explanation:
"I use a dictionary where the key is the sorted character tuple of each word (e.g. `tuple(sorted(word))`).
For each word in the list, I append it under its sorted tuple key using `result.setdefault(key, []).append(word)`.
Finally, I return `list(result.values())`."
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

if __name__ == "__main__":
    words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Words list:", words_list)
    print("Grouped Anagrams:", group_anagrams(words_list))
