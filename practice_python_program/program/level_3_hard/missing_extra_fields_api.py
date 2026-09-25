"""
37. Find Missing and Extra Fields in API Response
Interview Note: Uses set difference (expected_keys - actual_keys and actual_keys - expected_keys) to validate schema payload completeness.
Time Complexity: O(e + a)
Space Complexity: O(e + a)
"""

def find_missing_and_extra_fields(expected: dict, actual: dict) -> tuple[set, set]:
    expected_keys = set(expected)
    actual_keys = set(actual)

    missing = expected_keys - actual_keys
    extra = actual_keys - expected_keys

    return missing, extra

if __name__ == "__main__":
    expected = {
        "id": 101,
        "name": "Neeraj",
        "email": "test@example.com",
        "status": "active"
    }
    actual = {
        "id": 101,
        "name": "Neeraj",
        "phone": "9999999999"
    }
    missing, extra = find_missing_and_extra_fields(expected, actual)
    print("Missing fields:", missing)
    print("Extra fields:", extra)
