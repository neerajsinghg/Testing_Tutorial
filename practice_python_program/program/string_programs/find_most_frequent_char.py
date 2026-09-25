"""
Interview Question: How do you find the most frequent character in a string?

Interview Explanation:
"I build a frequency counter dictionary `count[char] = count.get(char, 0) + 1` for characters (ignoring spaces if requested).
I return `max(count, key=count.get)`."
"""

def most_frequent_char(text: str, ignore_spaces: bool = True) -> str | None:
    count = {}
    for char in text:
        if ignore_spaces and char.isspace():
            continue
        count[char] = count.get(char, 0) + 1
    return max(count, key=count.get) if count else None

if __name__ == "__main__":
    text = "selenium automation testing"
    print("Text:", text)
    print("Most Frequent Character:", most_frequent_char(text))
