"""
Interview Question: How do you find duplicate IDs in an API JSON response array?

Interview Explanation:
"When validating API endpoint returns (e.g. GET /users returning a list of user objects), IDs must be unique.
I iterate over the list of user dictionaries using a `seen` set. If an ID is already in `seen`, I flag it as a duplicate.
Set membership lookup operates in O(1) time."
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
    users_response = [
        {"id": 101, "name": "A"},
        {"id": 102, "name": "B"},
        {"id": 101, "name": "C"},
        {"id": 103, "name": "D"}
    ]

    dups = find_duplicate_ids(users_response)
    print("Duplicate IDs found in response:", dups)
