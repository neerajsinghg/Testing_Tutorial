# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s):
    char_index_map = {}
    start = 0
    max_len = 0

    for idx, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = idx
        max_len = max(max_len, idx - start + 1)

    return max_len

s = "abcabcbb"
print(longest_substring(s))