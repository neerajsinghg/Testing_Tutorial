"""
Find Duplicate Values in a Dictionary
Interview Note: Iterates through dict.values() using a seen set and collects duplicate values into a result set.
Time Complexity: O(v)
Space Complexity: O(v)
"""

def find_duplicate_values(data: dict) -> set:
    seen = set()
    duplicates = set()
    for value in data.values():
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates

if __name__ == "__main__":
    data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
    print("Duplicate Values:", find_duplicate_values(data))
