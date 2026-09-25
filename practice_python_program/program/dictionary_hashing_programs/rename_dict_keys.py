"""
Interview Question: How do you rename keys in a dictionary using a mapping schema in Python?

Interview Explanation:
"I iterate through items in the dictionary. If a key exists in `key_mapping`, I use `key_mapping[old_key]` as the new key name.
Otherwise, I retain the `old_key`."
"""

def rename_dictionary_keys(data: dict, key_mapping: dict[str, str]) -> dict:
    return {key_mapping.get(k, k): v for k, v in data.items()}

if __name__ == "__main__":
    db_record = {"emp_id": 101, "emp_name": "Neeraj", "usr_status": "ACTIVE"}
    mapping = {"emp_id": "id", "emp_name": "name", "usr_status": "status"}
    print("DB Record:", db_record)
    print("Renamed API Contract Record:", rename_dictionary_keys(db_record, mapping))
