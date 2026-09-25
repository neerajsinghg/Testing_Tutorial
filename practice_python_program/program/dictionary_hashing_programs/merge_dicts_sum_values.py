"""
Merge Dictionaries and Sum Common Values
Interview Note: Copies first dictionary and adds values from second dictionary using `get(key, 0) + value`.
Time Complexity: O(k1 + k2)
Space Complexity: O(k1 + k2)
"""

def merge_and_sum(d1: dict, d2: dict) -> dict:
    result = d1.copy()
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    return result

if __name__ == "__main__":
    d1 = {"a": 10, "b": 20}
    d2 = {"b": 30, "c": 40}
    print("Merged and Summed Dict:", merge_and_sum(d1, d2))
