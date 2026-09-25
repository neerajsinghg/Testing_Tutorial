"""
Find Longest Common Prefix Among Array of Strings
Interview Note: Initializes prefix with first word and truncates prefix character by character using startswith().
Time Complexity: O(N * M) where N is word count, M is shortest word length.
Space Complexity: O(1)
"""

def longest_common_prefix(words: list[str]) -> str:
    if not words:
        return ""
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    words = ["flower", "flow", "flight"]
    print("Words:", words)
    print("Longest Common Prefix:", longest_common_prefix(words))
