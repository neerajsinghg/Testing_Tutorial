"""
Find Common Keys with Same Values Between Two Dictionaries
Interview Note: Uses set comprehension `key for key in d1 if key in d2 and d1[key] == d2[key]`.
Time Complexity: O(k1)
Space Complexity: O(c)
"""

def common_keys_matching_values(d1: dict, d2: dict) -> set:
    return {key for key in d1 if key in d2 and d1[key] == d2[key]}

if __name__ == "__main__":
    d1 = {"a": 10, "b": 20, "c": 30}
    d2 = {"a": 10, "b": 50, "c": 30}
    print("Common keys with same values:", common_keys_matching_values(d1, d2))
