"""
6. Find First Non-Repeating Character
Interview Note: Uses two passes: pass 1 counts frequency, pass 2 finds the first char with count 1.
Time Complexity: O(n)
Space Complexity: O(u)
"""

def first_non_repeating(text: str) -> str | None:
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
        
    for char in text:
        if count[char] == 1:
            return char
    return None

if __name__ == "__main__":
    text = "aabbcde"
    result = first_non_repeating(text)
    print("First non-repeating character:", result)
