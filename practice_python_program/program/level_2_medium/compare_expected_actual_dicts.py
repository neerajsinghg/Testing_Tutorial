"""
30. Compare Expected and Actual Dictionaries
Interview Note: Crucial for API testing assertions. Iterates through expected keys and checks for value equality against actual dict.
Time Complexity: O(k)
Space Complexity: O(1)
"""

def compare_dictionaries(expected: dict, actual: dict) -> list[str]:
    mismatches = []
    for key in expected:
        if expected[key] != actual.get(key):
            mismatches.append(f"Key '{key}' mismatch | Expected: {expected[key]}, Actual: {actual.get(key)}")
    return mismatches

if __name__ == "__main__":
    expected = {"status": "success", "count": 10}
    actual = {"status": "success", "count": 8}
    
    diffs = compare_dictionaries(expected, actual)
    if diffs:
        for diff in diffs:
            print(diff)
    else:
        print("Dictionaries match perfectly!")
