"""
Interview Question: How do you safely fetch a value from a deeply nested dictionary using a dot-separated key string?

Interview Explanation:
"I split the path string (e.g. `'user.address.city'`) by `.` and traverse the dictionary layer by layer.
If at any point a key is missing or the current node is not a dictionary, I safely return `default_value` instead of raising KeyError."
"""

from typing import Any

def get_nested_value(data: dict, path: str, default: Any = None) -> Any:
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == "__main__":
    user_json = {
        "user": {
            "profile": {
                "name": "Neeraj",
                "settings": {"theme": "dark"}
            }
        }
    }
    print("Fetched Theme:", get_nested_value(user_json, "user.profile.settings.theme"))
    print("Fetched Non-existent Key:", get_nested_value(user_json, "user.profile.age", default=30))
