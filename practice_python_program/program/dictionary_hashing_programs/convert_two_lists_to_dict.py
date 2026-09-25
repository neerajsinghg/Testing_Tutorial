"""
Interview Question: How do you combine two parallel lists (keys and values) into a single dictionary in Python?

Interview Explanation:
"I use `dict(zip(keys_list, values_list))` or dictionary comprehension `{k: v for k, v in zip(keys, values)}`.
`zip()` pairs corresponding items up to the shortest list length."
"""

def create_dict_from_lists(keys: list, values: list) -> dict:
    return dict(zip(keys, values))

if __name__ == "__main__":
    fields = ["id", "username", "status", "role"]
    data = [101, "neeraj_sdet", "active", "lead"]
    print("Keys:", fields)
    print("Values:", data)
    print("Combined Dict:", create_dict_from_lists(fields, data))
