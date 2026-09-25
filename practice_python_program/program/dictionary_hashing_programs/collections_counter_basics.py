"""
Interview Question: How do you use `collections.Counter` for frequency counting and extracting top elements?

Interview Explanation:
"`collections.Counter` is a specialized dictionary subclass for counting hashable objects.
It provides `counter.most_common(n)` to retrieve the top n frequent items and supports mathematical set operators."
"""

from collections import Counter

def analyze_test_statuses(statuses: list[str]):
    counter = Counter(statuses)
    print("Status Frequencies:", dict(counter))
    print("Most Common Status:", counter.most_common(1))
    return counter

if __name__ == "__main__":
    results = ["PASS", "PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]
    analyze_test_statuses(results)
