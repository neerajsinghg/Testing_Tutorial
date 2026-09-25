"""
4. Count Characters in a String
Interview Note: Uses a dictionary (hash map) to build a frequency distribution.
Time Complexity: O(n)
Space Complexity: O(u) where u is number of unique characters.
"""

def count_characters(text: str) -> dict:
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count

if __name__ == "__main__":
    text = "automation"
    print("Character Counts:", count_characters(text))
