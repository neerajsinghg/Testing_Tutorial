"""
Interview Question: How do you verify if ALL required keys exist in a dictionary using Python built-ins?

Interview Explanation:
"I use `all(key in data for key in required_keys)` or `set(required_keys).issubset(data.keys())`.
`all()` short-circuits on the first missing key, operating efficiently in O(K) time."
"""

def all_keys_exist(data: dict, required_keys: list[str]) -> bool:
    return all(key in data for key in required_keys)

if __name__ == "__main__":
    required = ["id", "name", "email", "role"]
    valid_payload = {"id": 1, "name": "Neeraj", "email": "a@b.com", "role": "admin"}
    invalid_payload = {"id": 1, "name": "Neeraj", "email": "a@b.com"}

    print("Valid payload check:", all_keys_exist(valid_payload, required))
    print("Invalid payload check:", all_keys_exist(invalid_payload, required))
