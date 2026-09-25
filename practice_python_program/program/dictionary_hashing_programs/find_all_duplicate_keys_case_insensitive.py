"""
Interview Question: How do you detect case-insensitive header key conflicts in API header dictionaries?

Interview Explanation:
"HTTP headers should be case-insensitive (e.g. `Content-Type` vs `content-type`).
I build a mapping of `lower_key -> list of original keys`. Any lower_key with list length > 1 represents a duplicate key conflict."
"""

from collections import defaultdict

def find_case_insensitive_header_conflicts(headers: dict) -> dict[str, list[str]]:
    key_map = defaultdict(list)
    for key in headers.keys():
        key_map[key.lower()].append(key)
    return {l_key: orig_keys for l_key, orig_keys in key_map.items() if len(orig_keys) > 1}

if __name__ == "__main__":
    headers_dict = {
        "Content-Type": "application/json",
        "content-type": "text/html",
        "Authorization": "Bearer 123",
        "authorization": "Bearer 456"
    }
    conflicts = find_case_insensitive_header_conflicts(headers_dict)
    print("Header Key Case Conflicts:", conflicts)
