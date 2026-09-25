"""
Interview Question: How do you group test cases by module name using Python dictionaries?

Interview Explanation:
"I iterate through the test case records list and use dictionary `setdefault(module, [])`
to dynamically initialize empty lists for new modules and append test names under their respective module keys."
"""

def group_tests_by_module(tests: list[dict]) -> dict[str, list[str]]:
    result = {}
    for test in tests:
        module = test["module"]
        result.setdefault(module, []).append(test["name"])
    return result

if __name__ == "__main__":
    tests_list = [
        {"name": "test_login", "module": "Auth"},
        {"name": "test_logout", "module": "Auth"},
        {"name": "test_search", "module": "Search"},
        {"name": "test_filter", "module": "Search"}
    ]

    grouped = group_tests_by_module(tests_list)
    print("Grouped Test Cases by Module:")
    for module, tests in grouped.items():
        print(f" Module '{module}': {tests}")
