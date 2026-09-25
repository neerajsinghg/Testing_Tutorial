"""
Interview Question: How do you check if a sentence is a pangram (contains all 26 letters of the alphabet)?

Interview Explanation:
"A pangram contains every letter from 'a' to 'z' at least once (e.g. 'The quick brown fox jumps over the lazy dog').
I extract all lowercase alphabetic characters into a set and check if `len(alphabet_set) == 26`."
"""

import string

def is_pangram(sentence: str) -> bool:
    alphabet_set = {char.lower() for char in sentence if char.isalpha()}
    return len(alphabet_set) == 26

if __name__ == "__main__":
    s1 = "The quick brown fox jumps over the lazy dog"
    s2 = "Hello world Python SDET"
    print(f"Is '{s1}' a pangram?", is_pangram(s1))
    print(f"Is '{s2}' a pangram?", is_pangram(s2))
