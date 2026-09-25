# Find duplicate keys from a list of dictionaries

users = [
    {"id": 101, "name": "A"},
    {"id": 102, "name": "B"},
    {"id": 101, "name": "C"},
    {"id": 103, "name": "D"}
]

def find_duplicate_keys3(users):
    seen = set()
    duplicates = set()

    for user in users:
        user_id = user["id"]

        if user_id in seen:
            duplicates.add(user_id)
        else:
            seen.add(user_id)
    return list(duplicates)

duplicate_keys3 = find_duplicate_keys3(users)
print("Duplicate keys (method 3):", duplicate_keys3)

def find_duplicate_keys(users, key):
    key_count = {}
    for user in users:
        value = user.get(key)
        if value is not None:
            key_count[value] = key_count.get(value, 0) + 1
    duplicate_keys = [value for value, count in key_count.items() if count > 1]
    return duplicate_keys

duplicate_keys = find_duplicate_keys(users, "id")
print("Duplicate keys:", duplicate_keys)

def find_duplicate_keys1(users, key):
    seen = set()
    duplicates = set()
    for user in users:
        value = user.get(key)
        if value is not None:
            if value in seen:
                duplicates.add(value)
            else:
                seen.add(value)
    return list(duplicates)

duplicate_keys1 = find_duplicate_keys1(users, "id")
print("Duplicate keys (method 2):", duplicate_keys1)