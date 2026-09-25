"""
32. Longest Substring Without Repeating Characters
Interview Note: Sliding window technique using left and right pointers with a set to track window contents.
Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m is character set size.
"""

def length_of_longest_substring(text: str) -> int:
    seen = set()
    left = 0
    maximum = 0

    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1
        seen.add(text[right])
        maximum = max(maximum, right - left + 1)

    return maximum

if __name__ == "__main__":
    text = "abcabcbb"
    print("Input String:", text)
    print("Longest Substring Length:", length_of_longest_substring(text))
