"""
Recursive Deep Diffing of Complex Nested JSON Payloads
Senior SDET Context: Recursively compares nested API JSON objects and arrays, pinpointing exact key paths with mismatched values.
"""

def deep_diff(dict1: dict | list, dict2: dict | list, path: str = "") -> list[str]:
    diffs = []
    if type(dict1) != type(dict2):
        return [f"[{path}] Type mismatch: {type(dict1).__name__} vs {type(dict2).__name__}"]

    if isinstance(dict1, dict):
        all_keys = set(dict1.keys()) | set(dict2.keys())
        for key in all_keys:
            current_path = f"{path}.{key}" if path else key
            if key not in dict1:
                diffs.append(f"[{current_path}] Key missing from expected dict")
            elif key not in dict2:
                diffs.append(f"[{current_path}] Key missing from actual dict")
            else:
                diffs.extend(deep_diff(dict1[key], dict2[key], current_path))
    elif isinstance(dict1, list):
        if len(dict1) != len(dict2):
            diffs.append(f"[{path}] Array length mismatch: {len(dict1)} vs {len(dict2)}")
        for idx, (item1, item2) in enumerate(zip(dict1, dict2)):
            diffs.extend(deep_diff(item1, item2, f"{path}[{idx}]"))
    else:
        if dict1 != dict2:
            diffs.append(f"[{path}] Value mismatch: Expected '{dict1}', Actual '{dict2}'")

    return diffs

if __name__ == "__main__":
    expected_json = {
        "user": {"name": "Neeraj", "roles": ["Admin", "QA"]},
        "config": {"theme": "dark", "timeout": 30}
    }
    actual_json = {
        "user": {"name": "Neeraj", "roles": ["Admin", "Dev"]},
        "config": {"theme": "light", "timeout": 30}
    }
    mismatches = deep_diff(expected_json, actual_json)
    print("Deep JSON Mismatches:")
    for diff in mismatches:
        print(" -", diff)
