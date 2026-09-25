"""
Interview Question: How do you aggregate numeric metrics by category key in a dictionary?

Interview Explanation:
"I iterate over execution records and accumulate totals in a dictionary `totals[category] = totals.get(category, 0.0) + duration`.
This is useful for summing suite execution durations or performance metrics per test class."
"""

def aggregate_durations_by_suite(records: list[dict]) -> dict[str, float]:
    summary = {}
    for record in records:
        suite = record["suite"]
        duration = record["duration"]
        summary[suite] = summary.get(suite, 0.0) + duration
    return summary

if __name__ == "__main__":
    test_runs = [
        {"suite": "Auth", "duration": 1.5},
        {"suite": "Search", "duration": 2.3},
        {"suite": "Auth", "duration": 0.8},
        {"suite": "Payment", "duration": 5.4}
    ]
    print("Aggregated Suite Durations:", aggregate_durations_by_suite(test_runs))
