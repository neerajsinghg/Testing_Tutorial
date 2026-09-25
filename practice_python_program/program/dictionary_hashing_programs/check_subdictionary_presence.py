"""
Interview Question: How do you verify if one dictionary is a sub-dictionary (subset of key-value claims) of another?

Interview Explanation:
"I check `subdict.items() <= full_dict.items()` using Python's built-in set view comparison.
Alternatively, I use all condition `all(full_dict.get(k) == v for k, v in subdict.items())`."
"""

def is_subdictionary(subdict: dict, full_dict: dict) -> bool:
    return subdict.items() <= full_dict.items()

if __name__ == "__main__":
    expected_claims = {"role": "admin", "status": "active"}
    api_response = {"id": 101, "name": "Neeraj", "role": "admin", "status": "active", "tenant": "us-east"}
    print("Expected Claims:", expected_claims)
    print("Is Sub-dictionary?", is_subdictionary(expected_claims, api_response))
