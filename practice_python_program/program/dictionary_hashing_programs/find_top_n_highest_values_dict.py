"""
Interview Question: How do you extract the top N keys with the highest values from a dictionary using heapq?

Interview Explanation:
"I use `heapq.nlargest(n, data.keys(), key=data.get)`.
This retrieves the top N keys ordered by their corresponding values in O(K log N) time."
"""

import heapq

def get_top_n_slow_tests(durations: dict[str, float], n: int = 3) -> list[tuple[str, float]]:
    top_keys = heapq.nlargest(n, durations.keys(), key=durations.get)
    return [(k, durations[k]) for k in top_keys]

if __name__ == "__main__":
    test_times = {
        "test_login": 1.2,
        "test_checkout": 8.5,
        "test_search": 3.1,
        "test_payment": 6.7,
        "test_reports": 12.4
    }
    print("Top 3 Slowest Tests:", get_top_n_slow_tests(test_times, n=3))
