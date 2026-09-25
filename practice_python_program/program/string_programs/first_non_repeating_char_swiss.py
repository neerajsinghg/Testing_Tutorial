"""
First Non-Repeating Character
Interview Note: Uses hash map frequency count followed by left-to-right scan to identify first unique character.
Time Complexity: O(n)
Space Complexity: O(u)
"""

def first_non_repeating_char(text: str) -> str | None:
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1

    for char in text:
        if count[char] == 1:
            return char
    return None

if __name__ == "__main__":
    text = "swiss"
    print(f"First non-repeating character in '{text}':", first_non_repeating_char(text))
