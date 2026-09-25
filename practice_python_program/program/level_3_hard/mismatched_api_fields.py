"""
38. Find Mismatched API Fields
Interview Note: Compares values for each key in expected dictionary against actual dictionary and records differences.
Time Complexity: O(k)
Space Complexity: O(m) where m is number of mismatches.
"""

def find_mismatched_fields(expected: dict, actual: dict) -> dict:
    mismatches = {}
    for key, expected_value in expected.items():
        actual_value = actual.get(key)
        if expected_value != actual_value:
            mismatches[key] = {
                "expected": expected_value,
                "actual": actual_value
            }
    return mismatches

if __name__ == "__main__":
    expected = {"status": "success", "count": 10}
    actual = {"status": "success", "count": 8}
    print("Mismatched Fields:", find_mismatched_fields(expected, actual))
