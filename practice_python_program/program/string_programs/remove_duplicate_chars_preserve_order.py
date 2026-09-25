"""
Remove Duplicate Characters While Preserving Order
Interview Note: Uses set for O(1) membership check combined with list buffer to maintain original character sequence.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def remove_duplicates_preserve_order(text: str) -> str:
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    text = "programming"
    print("Original:", text)
    print("Unique chars preserved order:", remove_duplicates_preserve_order(text))
