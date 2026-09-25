"""
Interview Question: How do you filter a dictionary by value conditions using dictionary comprehension in Python?

Interview Explanation:
"I use dictionary comprehension `{key: val for key, val in data.items() if condition}`.
For instance, filtering test execution metrics where `execution_time > 5.0` allows identifying slow running tests."
"""

def filter_slow_tests(test_durations: dict[str, float], threshold: float = 5.0) -> dict[str, float]:
    return {test: duration for test, duration in test_durations.items() if duration > threshold}

if __name__ == "__main__":
    durations = {
        "test_login": 1.2,
        "test_checkout": 8.5,
        "test_search": 3.1,
        "test_payment": 6.7
    }
    print("All Durations:", durations)
    print("Slow Tests (> 5.0s):", filter_slow_tests(durations, threshold=5.0))
