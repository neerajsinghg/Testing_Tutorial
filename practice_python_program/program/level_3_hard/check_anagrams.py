"""
33. Check Whether Two Strings Are Anagrams
Interview Note: Demonstrates both sorted approach O(n log n) and frequency map approach O(n).
Time Complexity: O(n)
Space Complexity: O(u)
"""

def build_frequency(text: str) -> dict:
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

def is_anagram(text1: str, text2: str) -> bool:
    return build_frequency(text1) == build_frequency(text2)

if __name__ == "__main__":
    t1, t2 = "listen", "silent"
    print(f"Are '{t1}' and '{t2}' anagrams?", is_anagram(t1, t2))
