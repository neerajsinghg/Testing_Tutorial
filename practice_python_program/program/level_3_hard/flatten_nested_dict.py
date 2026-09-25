"""
39. Flatten a Nested Dictionary
Interview Note: Uses recursion to concatenate dot-separated key prefixes (e.g. user.address.city).
Time Complexity: O(N) where N total primitive key-value pairs.
Space Complexity: O(D) stack depth.
"""

def flatten_dict(data: dict, parent: str = "") -> dict:
    result = {}
    for key, value in data.items():
        new_key = f"{parent}.{key}" if parent else key
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key))
        else:
            result[new_key] = value
    return result

if __name__ == "__main__":
    data = {
        "user": {
            "name": "Neeraj",
            "address": {
                "city": "Gurugram"
            }
        }
    }
    print("Nested Dict:", data)
    print("Flattened Dict:", flatten_dict(data))
