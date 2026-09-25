"""
41. Find Failed Test Cases
Interview Note: List comprehension filtering dictionary entries where status == 'FAIL'.
Time Complexity: O(n)
Space Complexity: O(f) where f is number of failed tests.
"""

def get_failed_tests(results: dict[str, str]) -> list[str]:
    return [test for test, status in results.items() if status == "FAIL"]

if __name__ == "__main__":
    results = {
        "test_login": "PASS",
        "test_search": "FAIL",
        "test_payment": "FAIL",
        "test_logout": "PASS"
    }
    print("Failed Tests:", get_failed_tests(results))
