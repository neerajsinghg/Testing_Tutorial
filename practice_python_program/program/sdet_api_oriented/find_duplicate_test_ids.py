"""
Find Duplicate Test Case IDs
Interview Note: Iterates through test case dict list and uses set tracking to flag duplicate IDs.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_duplicate_test_ids(test_cases: list[dict]) -> list[int]:
    seen = set()
    duplicates = []
    for test in test_cases:
        test_id = test["id"]
        if test_id in seen:
            duplicates.append(test_id)
        seen.add(test_id)
    return duplicates

if __name__ == "__main__":
    test_cases = [
        {"id": 101, "name": "Login"},
        {"id": 102, "name": "Search"},
        {"id": 101, "name": "Login Again"}
    ]
    print("Duplicate Test IDs:", find_duplicate_test_ids(test_cases))
