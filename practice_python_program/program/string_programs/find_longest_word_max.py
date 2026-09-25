"""
Find Longest Word using max(key=len)
Interview Note: Uses max() built-in with len as key function to find longest token.
Time Complexity: O(n)
Space Complexity: O(w)
"""

def find_longest_word(sentence: str) -> str:
    words = sentence.split()
    return max(words, key=len) if words else ""

if __name__ == "__main__":
    sentence = "Python Selenium Automation Framework"
    print("Longest Word:", find_longest_word(sentence))
