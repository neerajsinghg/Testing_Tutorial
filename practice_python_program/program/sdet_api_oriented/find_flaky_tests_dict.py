"""
Find Flaky Tests
Interview Note: Detects test names whose historical status list contains both PASS and FAIL results.
Time Complexity: O(t * r)
Space Complexity: O(f)
"""

def get_flaky_tests(results: dict[str, list[str]]) -> list[str]:
    return [test for test, statuses in results.items() if "PASS" in statuses and "FAIL" in statuses]

if __name__ == "__main__":
    results = {
        "test_login": ["PASS", "PASS"],
        "test_search": ["PASS", "FAIL", "PASS"],
        "test_payment": ["FAIL", "FAIL"]
    }
    print("Flaky Tests:", get_flaky_tests(results))
