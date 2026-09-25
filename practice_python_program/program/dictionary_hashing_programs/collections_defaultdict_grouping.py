"""
Interview Question: How do you group items using `collections.defaultdict` without raising KeyError?

Interview Explanation:
"`defaultdict(list)` or `defaultdict(set)` automatically initializes missing keys with empty lists or sets upon first access.
This eliminates manual key existence checks `if key not in dict: dict[key] = []`."
"""

from collections import defaultdict

def group_tests_by_severity(tests: list[dict]) -> dict[str, list[str]]:
    severity_map = defaultdict(list)
    for test in tests:
        severity_map[test["severity"]].append(test["name"])
    return dict(severity_map)

if __name__ == "__main__":
    test_cases = [
        {"name": "test_payment", "severity": "CRITICAL"},
        {"name": "test_footer_links", "severity": "LOW"},
        {"name": "test_login", "severity": "CRITICAL"},
        {"name": "test_profile_picture", "severity": "MEDIUM"}
    ]
    print("Grouped Test Cases:", group_tests_by_severity(test_cases))
