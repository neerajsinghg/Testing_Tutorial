"""
Interview Question: How do you aggregate and count test execution results (PASS, FAIL, SKIP) in Python?

Interview Explanation:
"I parse the list of execution status strings using a dictionary frequency accumulator `summary[status] = summary.get(status, 0) + 1`.
This aggregates suite metrics to generate summary reports or publish CI pipeline metrics."
"""

def summarize_test_results(results: list[str]) -> dict[str, int]:
    summary = {}
    for status in results:
        summary[status] = summary.get(status, 0) + 1
    return summary

if __name__ == "__main__":
    execution_results = ["PASS", "PASS", "FAIL", "PASS", "SKIP", "FAIL"]
    report = summarize_test_results(execution_results)
    print("Test Execution Summary:", report)
