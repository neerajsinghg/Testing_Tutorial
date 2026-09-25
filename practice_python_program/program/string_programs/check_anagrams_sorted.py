"""
Check Anagrams using Sorting
Interview Note: Comparing sorted characters checks if both strings contain exact same character counts.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1, s2 = "listen", "silent"
    print(f"Are '{s1}' and '{s2}' anagrams?", is_anagram(s1, s2))
