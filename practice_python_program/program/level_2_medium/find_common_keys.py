"""
29. Find Common Keys Between Two Dictionaries
Interview Note: Takes set intersection (&) of dict.keys() views.
Time Complexity: O(min(k1, k2))
Space Complexity: O(min(k1, k2))
"""

def find_common_keys(dict1: dict, dict2: dict) -> set:
    return dict1.keys() & dict2.keys()

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 20, "c": 30, "d": 40}
    print("Common Keys:", find_common_keys(dict1, dict2))
