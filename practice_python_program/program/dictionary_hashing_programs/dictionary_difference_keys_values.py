"""
Interview Question: How do you compute the symmetric difference between two dictionaries in Python?

Interview Explanation:
"I inspect keys and values from both dictionaries:
1. Keys present in dict1 but missing in dict2.
2. Keys present in dict2 but missing in dict1.
3. Common keys where `dict1[key] != dict2[key]`.
I store all differences in a structured report dictionary."
"""

def compute_dict_difference(dict1: dict, dict2: dict) -> dict:
    keys1, keys2 = set(dict1.keys()), set(dict2.keys())
    only_in_1 = keys1 - keys2
    only_in_2 = keys2 - keys1
    common_keys = keys1 & keys2

    value_mismatches = {k: {"dict1": dict1[k], "dict2": dict2[k]} for k in common_keys if dict1[k] != dict2[k]}

    return {
        "only_in_dict1": {k: dict1[k] for k in only_in_1},
        "only_in_dict2": {k: dict2[k] for k in only_in_2},
        "value_mismatches": value_mismatches
    }

if __name__ == "__main__":
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 20, "c": 3, "d": 4}
    print("Symmetric Dictionary Difference:", compute_dict_difference(d1, d2))
