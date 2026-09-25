"""
42. Find Flaky Tests
Interview Note: Identifies tests whose historical run results contain both 'PASS' and 'FAIL'.
Time Complexity: O(t * r) where t is test count, r is runs per test.
Space Complexity: O(f)
"""

def identify_flaky_tests(results: dict[str, list[str]]) -> list[str]:
    flaky = []
    for test, statuses in results.items():
        if "PASS" in statuses and "FAIL" in statuses:
            flaky.append(test)
    return flaky

if __name__ == "__main__":
    results = {
        "test_login": ["PASS", "PASS", "PASS"],
        "test_search": ["PASS", "FAIL", "PASS"],
        "test_payment": ["FAIL", "FAIL", "FAIL"]
    }
    print("Flaky Tests:", identify_flaky_tests(results))
