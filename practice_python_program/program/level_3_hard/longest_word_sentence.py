"""
31. Find Longest Word in a Sentence
Interview Note: Splits sentence into words and maintains tracking variable for longest word.
Time Complexity: O(n)
Space Complexity: O(w)
"""

def find_longest_word(sentence: str) -> str:
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == "__main__":
    sentence = "Python Selenium automation framework"
    print("Sentence:", sentence)
    print("Longest Word:", find_longest_word(sentence))
