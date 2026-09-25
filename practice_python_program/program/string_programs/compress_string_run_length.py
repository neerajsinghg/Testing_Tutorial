"""
Interview Question: How do you perform basic string compression using character counts (Run-Length Encoding)?

Interview Explanation:
"I iterate through the string tracking the current character and its consecutive count.
When the character changes or at the end of the loop, I append the character and its count to a result list.
If the compressed string is not shorter than the original, I return the original string."
"""

def compress_string(text: str) -> str:
    if not text:
        return ""

    compressed = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")

    result = "".join(compressed)
    return result if len(result) < len(text) else text

if __name__ == "__main__":
    sample = "aabcccccaaa"
    print("Original:", sample)
    print("Compressed:", compress_string(sample))
