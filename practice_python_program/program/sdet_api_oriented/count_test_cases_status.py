"""
Count Test Execution Results (PASS/FAIL/SKIP)
Interview Note: Aggregates test statuses using dictionary counter pattern.
Time Complexity: O(n)
Space Complexity: O(s)
"""

def count_test_status(results: list[str]) -> dict[str, int]:
    summary = {}
    for result in results:
        summary[result] = summary.get(result, 0) + 1
    return summary

if __name__ == "__main__":
    results = ["PASS", "PASS", "FAIL", "PASS", "SKIP", "FAIL"]
    print("Execution Summary:", count_test_status(results))
