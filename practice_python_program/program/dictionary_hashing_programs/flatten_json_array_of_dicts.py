"""
Interview Question: How do you extract a specific column/key list from a list of JSON dictionaries in Python?

Interview Explanation:
"I use list comprehension `[item[target_key] for item in json_array if target_key in item]`.
For example, extracting all user email strings from a GET /users API response array."
"""

def extract_field_from_json_array(records: list[dict], target_key: str) -> list:
    return [item[target_key] for item in records if target_key in item]

if __name__ == "__main__":
    users_json = [
        {"id": 1, "name": "Neeraj", "email": "neeraj@test.com"},
        {"id": 2, "name": "Rahul", "email": "rahul@test.com"},
        {"id": 3, "name": "Amit", "email": "amit@test.com"}
    ]
    emails = extract_field_from_json_array(users_json, "email")
    print("Extracted Email List:", emails)
