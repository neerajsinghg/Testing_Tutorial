"""
40. Count Test Execution Results
Interview Note: Aggregates status counters (PASS, FAIL, SKIP) for test suite metrics.
Time Complexity: O(n)
Space Complexity: O(s) where s is number of distinct statuses.
"""

def summarize_results(results: list[str]) -> dict[str, int]:
    summary = {}
    for status in results:
        summary[status] = summary.get(status, 0) + 1
    return summary

if __name__ == "__main__":
    results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]
    print("Test Summary:", summarize_results(results))
