"""
Check Whether One String is Rotation of Another
Interview Note: Checks length equality and substring presence in concatenated string s1 + s1.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)

if __name__ == "__main__":
    s1, s2 = "abcd", "cdab"
    print(f"Is '{s2}' a rotation of '{s1}'?", is_rotation(s1, s2))
