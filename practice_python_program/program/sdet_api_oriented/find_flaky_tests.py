"""
Interview Question: How do you identify flaky test cases from execution history logs?

Interview Explanation:
"A test is flaky if its execution history contains both 'PASS' and 'FAIL' outcomes across re-runs.
I iterate through a dictionary mapping test names to their status list, checking `if 'PASS' in statuses and 'FAIL' in statuses`.
Tests satisfying this condition are flagged for triage."
"""

def identify_flaky_tests(results: dict[str, list[str]]) -> list[str]:
    flaky = []
    for test, statuses in results.items():
        if "PASS" in statuses and "FAIL" in statuses:
            flaky.append(test)
    return flaky

if __name__ == "__main__":
    test_history = {
        "test_login": ["PASS", "PASS", "PASS"],
        "test_search": ["PASS", "FAIL", "PASS"],
        "test_payment": ["FAIL", "FAIL", "FAIL"]
    }

    flaky_tests = identify_flaky_tests(test_history)
    print("Flaky Test Cases Identified:", flaky_tests)
