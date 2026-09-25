"""
Valid Parentheses (Stack Matching)
Interview Note: Pushes opening brackets onto stack and pops to match closing bracket pairs using hash map.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid_parentheses(text: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack

if __name__ == "__main__":
    test1 = "({[]})"
    test2 = "({[}])"
    print(f"'{test1}' valid?", is_valid_parentheses(test1))
    print(f"'{test2}' valid?", is_valid_parentheses(test2))
