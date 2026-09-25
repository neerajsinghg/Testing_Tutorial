"""
Convert List of Dictionaries into a Lookup Dictionary
Interview Note: Transforms JSON/API array of objects into a key-indexed map for fast O(1) lookups.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def index_users_by_id(users: list[dict], key_field: str = "id", value_field: str = "name") -> dict:
    return {user[key_field]: user[value_field] for user in users}

if __name__ == "__main__":
    users = [
        {"id": 101, "name": "Amit"},
        {"id": 102, "name": "Neeraj"},
        {"id": 103, "name": "Rahul"}
    ]
    print("Indexed Users Map:", index_users_by_id(users))
