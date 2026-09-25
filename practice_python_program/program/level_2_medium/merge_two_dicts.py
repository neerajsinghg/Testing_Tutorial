"""
28. Merge Two Dictionaries
Interview Note: Python 3.9+ dictionary union operator (|) or unpack operator (**).
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    return dict1 | dict2

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    print("Dict 1:", dict1)
    print("Dict 2:", dict2)
    print("Merged:", merge_dictionaries(dict1, dict2))
