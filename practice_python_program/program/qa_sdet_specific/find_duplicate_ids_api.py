"""
44. Find Duplicate IDs in API Response
Interview Note: Uses a set to detect non-unique record identifiers in API JSON arrays.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_duplicate_ids(users: list[dict]) -> list[int]:
    seen = set()
    duplicates = []
    for user in users:
        user_id = user["id"]
        if user_id in seen:
            duplicates.append(user_id)
        seen.add(user_id)
    return duplicates

if __name__ == "__main__":
    users = [
        {"id": 101, "name": "A"},
        {"id": 102, "name": "B"},
        {"id": 101, "name": "C"},
        {"id": 103, "name": "D"}
    ]
    print("Duplicate IDs:", find_duplicate_ids(users))
