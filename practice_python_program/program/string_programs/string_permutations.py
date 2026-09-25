"""
Interview Question: How do you generate all permutations of a string in Python?

Interview Explanation:
"I can use Python's built-in `itertools.permutations(text)` or a recursive backtracking function.
For each character in the string, I pick it as the starting character and recursively permute the remaining substring."
"""

from itertools import permutations

def get_permutations_itertools(text: str) -> list[str]:
    return ["".join(p) for p in permutations(text)]

def get_permutations_recursive(text: str) -> list[str]:
    if len(text) <= 1:
        return [text]
    result = []
    for i, char in enumerate(text):
        remaining = text[:i] + text[i+1:]
        for sub_perm in get_permutations_recursive(remaining):
            result.append(char + sub_perm)
    return result

if __name__ == "__main__":
    s = "abc"
    print(f"Permutations of '{s}':", get_permutations_recursive(s))
