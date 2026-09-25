"""
Interview Question: How do you filter and extract failed test cases from a test suite execution dictionary?

Interview Explanation:
"I use Python list comprehension `[test for test, status in results.items() if status == 'FAIL']`.
This filters tests whose status equals 'FAIL' so they can be re-run automatically or exported to Jira."
"""

def get_failed_tests(results: dict[str, str]) -> list[str]:
    return [test for test, status in results.items() if status == "FAIL"]

if __name__ == "__main__":
    suite_results = {
        "test_login": "PASS",
        "test_search": "FAIL",
        "test_payment": "FAIL",
        "test_logout": "PASS"
    }

    failed_list = get_failed_tests(suite_results)
    print("Failed Test Cases:", failed_list)
